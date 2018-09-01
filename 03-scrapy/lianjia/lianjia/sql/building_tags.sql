/*
 Navicat Premium Data Transfer

 Source Server         : djangostudy
 Source Server Type    : MySQL
 Source Server Version : 80011
 Source Host           : 127.0.0.1:3306
 Source Schema         : lianjia

 Target Server Type    : MySQL
 Target Server Version : 80011
 File Encoding         : 65001

 Date: 01/09/2018 15:07:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for building_tags
-- ----------------------------
DROP TABLE IF EXISTS `building_tags`;
CREATE TABLE `building_tags`  (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `building_id` int(50) NULL DEFAULT NULL,
  `tag_id` int(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of building_tags
-- ----------------------------
INSERT INTO `building_tags` VALUES (1, 1, 1);
INSERT INTO `building_tags` VALUES (2, 1, 2);
INSERT INTO `building_tags` VALUES (3, 1, 3);

SET FOREIGN_KEY_CHECKS = 1;
