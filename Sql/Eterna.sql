-- Table for USERS
CREATE TABLE USERS (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for SERVICE_PROVIDERS
CREATE TABLE SERVICE_PROVIDERS (
    provider_id BIGSERIAL PRIMARY KEY,
    provider_type VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    status VARCHAR(50) NOT NULL,
    background_verification VARCHAR(50) NOT NULL
);

-- Table for SERVICES
CREATE TABLE SERVICES (
    service_id BIGSERIAL PRIMARY KEY,
    service_name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(100),
    base_price DECIMAL(10, 2) NOT NULL
);

-- Table for ADMINS
CREATE TABLE ADMINS (
    admin_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);

-- Junction Table for PROVIDER_SERVICES
CREATE TABLE PROVIDER_SERVICES (
    provider_service_id BIGSERIAL PRIMARY KEY,
    provider_id BIGINT NOT NULL,
    service_id BIGINT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (provider_id) REFERENCES SERVICE_PROVIDERS(provider_id),
    FOREIGN KEY (service_id) REFERENCES SERVICES(service_id),
    UNIQUE (provider_id, service_id)
);

-- Table for BOOKINGS
CREATE TABLE BOOKINGS (
    booking_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    provider_id BIGINT NOT NULL,
    service_id BIGINT NOT NULL,
    scheduled_time TIMESTAMP WITH TIME ZONE NOT NULL,
    booking_status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES USERS(user_id),
    FOREIGN KEY (provider_id) REFERENCES SERVICE_PROVIDERS(provider_id),
    FOREIGN KEY (service_id) REFERENCES SERVICES(service_id)
);

-- Table for REVIEWS
CREATE TABLE REVIEWS (
    review_id BIGSERIAL PRIMARY KEY,
    booking_id BIGINT NOT NULL UNIQUE,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES BOOKINGS(booking_id)
);

-- Table for SERVICE_REPORT
CREATE TABLE SERVICE_REPORT (
    report_id BIGSERIAL PRIMARY KEY,
    booking_id BIGINT NOT NULL UNIQUE,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES BOOKINGS(booking_id)
);

-- Table for COMPLAINTS
CREATE TABLE COMPLAINTS (
    complaint_id BIGSERIAL PRIMARY KEY,
    booking_id BIGINT NOT NULL UNIQUE,
    user_id BIGINT NOT NULL,
    provider_id BIGINT NOT NULL,
    complaint_text TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES BOOKINGS(booking_id),
    FOREIGN KEY (user_id) REFERENCES USERS(user_id),
    FOREIGN KEY (provider_id) REFERENCES SERVICE_PROVIDERS(provider_id)
);