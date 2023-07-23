-- A script that converts the 'hbtn_0c_0' database to UTF-8 
-- (utf8mb4, collate utf8mb4_unicode_ci) in my MySQL server.
-- This script was not executed locally.
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
