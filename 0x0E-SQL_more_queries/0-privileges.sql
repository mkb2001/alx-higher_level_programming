-- this is a script about privileges
SELECT * FROM information_schema.user_privileges WHERE grantee IN ('user_0d_1@\'%\'', 'user_0d_2@\'%\'');
