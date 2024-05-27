-- this is a script that converts the encoding of a database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER  SET = utfmb4 COLLATE = utfmb4_unicode_ci;
ALTER DATABASE hbtn_0c_0.first_table COLLATE utf8mb4_unicode_ci;
ALTER DATABASE hbtn_0c_0.first_table MODIFY COLUMN 'name' VARCHAR(256) COLLATE utf8mb4_unicode_ci
