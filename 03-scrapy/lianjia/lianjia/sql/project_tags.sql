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

 Date: 01/09/2018 15:08:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for project_tags
-- ----------------------------
DROP TABLE IF EXISTS `project_tags`;
CREATE TABLE `project_tags`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `desc`(`tag`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of project_tags
-- ----------------------------
INSERT INTO `project_tags` VALUES (1, '低密度');
INSERT INTO `project_tags` VALUES (4, '地铁房');
INSERT INTO `project_tags` VALUES (3, '花园洋房');
INSERT INTO `project_tags` VALUES (2, '车位充足');

SET FOREIGN_KEY_CHECKS = 1;
