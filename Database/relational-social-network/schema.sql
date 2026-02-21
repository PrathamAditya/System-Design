-- CREATE DATABASE social_media_db;
-- USE social_media_db;

-- CREATE TABLE users (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(50) NOT NULL,
--     postcount INT NOT NULL DEFAULT 0 CHECK (postcount >= 0),
--     socialhandle VARCHAR(50) NOT NULL UNIQUE
-- );

-- CREATE TABLE posts (
--     post_id INT PRIMARY KEY AUTO_INCREMENT,
--     user_id INT NOT NULL,
--     post TEXT NOT NULL,
--     post_description TEXT,
--     FOREIGN KEY (user_id) 
--         REFERENCES users(id)
--         ON DELETE CASCADE
-- );

-- CREATE TABLE profile (
--     user_id INT PRIMARY KEY, --    only 1 profile per user
--     profile_photo TEXT NOT NULL,
--     FOREIGN KEY (user_id) --       if the user gets deleted the profile will also
--         REFERENCES users(id)
--         ON DELETE CASCADE
-- );

-- CREATE TABLE following (
--     user_id INT NOT NULL,
--     follower_id INT NOT NULL,
--     
--     PRIMARY KEY (user_id, follower_id),

--     FOREIGN KEY (user_id)
--         REFERENCES users(id)
--         ON DELETE CASCADE,

--     FOREIGN KEY (follower_id)
--         REFERENCES users(id)
--         ON DELETE CASCADE,

--     CHECK (user_id <> follower_id)        -- prevent self follow
-- )

-- transactions
START TRANSACTION;
INSERT INTO users (name, socialhandle) VALUES('AMOEBA', '_amoeba');
INSERT INTO profile (user_id, profile_photo) VALUES (LAST_INSERT_ID(), 'dp_photo_link');
COMMIT;

-- breaking it
START TRANSACTION;
INSERT INTO users (name, socialhandle)
VALUES ('TestUser', 'duplicate_handle');
INSERT INTO profile (user_id, profile_photo)
VALUES (999999, 'invalid_fk');  -- this will fail
COMMIT;

select * from users;