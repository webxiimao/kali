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

 Date: 01/09/2018 15:07:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for building
-- ----------------------------
DROP TABLE IF EXISTS `building`;
CREATE TABLE `building`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `address` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `average_price` int(50) NULL DEFAULT NULL,
  `average_price_unit` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `city_id` int(10) NULL DEFAULT NULL,
  `district_id` int(10) NULL DEFAULT NULL,
  `house_type` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `resblock_name` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `max_area` int(10) NULL DEFAULT NULL,
  `min_area` int(10) NULL DEFAULT NULL,
  `create_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `open_time` date NULL DEFAULT NULL,
  `status` int(2) NULL DEFAULT 0,
  `total_price_start` int(50) NULL DEFAULT NULL,
  `total_price_start_unit` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `isDelete` int(2) NULL DEFAULT 0,
  `county_id` int(10) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of building
-- ----------------------------
INSERT INTO `building` VALUES (1, '龙城大道', 130027, '元/平起', 1, 3, '商业区', '东海国际公寓', 140, 120, '2018-09-01 14:05:30', '2018-08-15', 1, 1830, '万/套起', 0, 1);

SET FOREIGN_KEY_CHECKS = 1;
