#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:15:44 2018

Name: khalednakhleh
"""

import json


def _parse_tfrecord(serialized_example):
    example = tf.parse_single_example(
        serialized_example,
        features={
            'image/encoded': tf.FixedLenFeature([], tf.string),
            'image/filename': tf.FixedLenFeature([], tf.string),
            'image/ID': tf.FixedLenFeature([], tf.string),
            'image/format': tf.FixedLenFeature([], tf.string),
            'image/height': tf.FixedLenFeature([], tf.int64),
            'image/width': tf.FixedLenFeature([], tf.int64),
            'image/channels': tf.FixedLenFeature([], tf.int64),
            'image/colorspace': tf.FixedLenFeature([], tf.string),
            'image/segmentation/class/encoded': tf.FixedLenFeature([], tf.string),
            'image/segmentation/class/format': tf.FixedLenFeature([], tf.string),
            })
    image = tf.image.decode_image(example['image/encoded'])
    image.set_shape([None, None, 3])
    label = tf.image.decode_image(example['image/segmentation/class/encoded'])
    label.set_shape([None, None, 1])
    image_float = tf.to_float(image)
    label_float = tf.to_float(label)
    return (image_float, label_float)

def _resize(image_dim):
    def _inner(images_orig, labels_orig):
        images = tf.image.resize_images(
                images=images_orig,
                size=[image_dim, image_dim],
                method=tf.image.ResizeMethod.BILINEAR)
        labels = tf.image.resize_images(
                images=labels_orig,
                size=[image_dim, image_dim],
                method=tf.image.ResizeMethod.BILINEAR)
        return (images, labels)
    return _inner

tfrecord_paths = json.load('./export.json')['tfrecord_paths']
test_set_size = math.ceil(0.2 * len(tfrecord_paths))
training_dataset = (tf.data.TFRecordDataset(tfrecord_paths)
  .skip(test_set_size)
  .map(_parse_tfrecord)
  .apply(tf.contrib.data.shuffle_and_repeat(50))
  .apply(tf.contrib.data.map_and_batch(_resize(512), 8)))