CREATE TABLE views (
  id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
  viewer_id MEDIUMINT UNSIGNED NOT NULL,
  view_datetime DATETIME NOT NULL,
  post_id MEDIUMINT UNSIGNED NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE posts (
  id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  post_text varchar(255) NOT NULL,
  times_seen int default 0,
  author_id MEDIUMINT UNSIGNED NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE users (
  id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
  username varchar(255) NOT NULL UNIQUE,
  email varchar(255) NOT NULL,
  profile_pic varchar(255) NOT NULL DEFAULT 'shorturl.at/OQRV5',
  user_type varchar(255) NOT NULL,
  user_password varchar(255) NOT NULL,
  last_login datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  is_logged_in boolean DEFAULT false,
  PRIMARY KEY (id)
);

INSERT INTO users (username, email, user_type, user_password)
VALUES ('admin', 'admin@sherpa.com', 'admin', 'admin');
