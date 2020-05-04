-- User table
CREATE TABLE `ongoingproject`.`tbl_user` (
  `user_id` BIGINT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL,
  `user_birthday` DATE NULL,
  `user_email` VARCHAR(45) NULL,
  `user_password` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`));


-- Feed table
CREATE TABLE `ongoingproject`.`tbl_post` (
  `post_id` BIGINT NULL AUTO_INCREMENT,
  `post_title` VARCHAR(45) NULL,
  `post_description` VARCHAR(45) NULL,
  PRIMARY KEY (`post_id`));