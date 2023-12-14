-- Creates the user user_0d_1 with all privileges

-- Check if the user user_0d_1 already exists
SELECT User FROM mysql.user WHERE User = 'user_0d_1';
IF FOUND_ROWS() = 0 THEN

    -- Create the user user_0d_1 with all privileges
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
    FLUSH PRIVILEGES;

END IF;
