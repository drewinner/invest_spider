CREATE TABLE `stock_base_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` char(10) NOT NULL DEFAULT '' COMMENT '代码',
  `name` varchar(45) NOT NULL DEFAULT '' COMMENT '名称',
  `pinyin` varchar(100) NOT NULL DEFAULT '' COMMENT '拼音首字母',
  `create_time` bigint(20) NOT NULL DEFAULT '-1' COMMENT '创建日期',
  `update_time` bigint(20) NOT NULL DEFAULT '-1' COMMENT '更新日期',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='股票基本信息表';