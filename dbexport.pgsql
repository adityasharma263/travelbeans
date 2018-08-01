--
-- PostgreSQL database dump
--

-- Dumped from database version 10.4 (Ubuntu 10.4-0ubuntu0.18.04)
-- Dumped by pg_dump version 10.4 (Ubuntu 10.4-0ubuntu0.18.04)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO priyanka;

--
-- Name: amenity; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.amenity (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    hotel_id integer,
    conference_room boolean,
    parking boolean,
    couple_friendly boolean,
    express_check_in_out boolean,
    laundry_service boolean,
    indoor_swimming_pool boolean,
    outdoor_swimming_pool boolean,
    porter_service boolean,
    "Room_cleaning_service" boolean,
    terrace boolean,
    child_baby_cot boolean,
    wheelchair_accessible boolean,
    doorman boolean,
    hairdresser boolean,
    banquets boolean,
    non_smoking_smoking_rooms boolean,
    pet_allowance boolean,
    lift boolean,
    bar boolean,
    gym boolean,
    pool boolean,
    restaurant boolean,
    spa boolean,
    wifi_in_lobby boolean,
    twenty_four_hr_reception boolean,
    twenty_four_hr_room_service boolean
);


ALTER TABLE public.amenity OWNER TO priyanka;

--
-- Name: amenity_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.amenity_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.amenity_id_seq OWNER TO priyanka;

--
-- Name: amenity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.amenity_id_seq OWNED BY public.amenity.id;


--
-- Name: cab; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.cab (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    car_name character varying,
    city character varying,
    car_type integer,
    cab_type integer,
    "desc" text
);


ALTER TABLE public.cab OWNER TO priyanka;

--
-- Name: cab_amenity; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.cab_amenity (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    cab_id integer,
    air_condition boolean,
    seater integer,
    baggage_allowance boolean,
    doorstep_delivery boolean,
    fuel boolean,
    fuel_type integer,
    fuel_capacity integer,
    automatic boolean,
    chauffeur boolean,
    verified_driver boolean
);


ALTER TABLE public.cab_amenity OWNER TO priyanka;

--
-- Name: cab_amenity_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.cab_amenity_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cab_amenity_id_seq OWNER TO priyanka;

--
-- Name: cab_amenity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.cab_amenity_id_seq OWNED BY public.cab_amenity.id;


--
-- Name: cab_booking; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.cab_booking (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    cab_id integer,
    one_way boolean,
    pickup_time timestamp with time zone NOT NULL,
    drop_time timestamp with time zone NOT NULL,
    outstation boolean,
    drop_latitude double precision,
    drop_longitude double precision,
    pickup_latitude double precision,
    pickup_longitude double precision
);


ALTER TABLE public.cab_booking OWNER TO priyanka;

--
-- Name: cab_booking_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.cab_booking_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cab_booking_id_seq OWNER TO priyanka;

--
-- Name: cab_booking_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.cab_booking_id_seq OWNED BY public.cab_booking.id;


--
-- Name: cab_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.cab_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cab_id_seq OWNER TO priyanka;

--
-- Name: cab_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.cab_id_seq OWNED BY public.cab.id;


--
-- Name: cab_image; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.cab_image (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    cab_id integer,
    image_url character varying
);


ALTER TABLE public.cab_image OWNER TO priyanka;

--
-- Name: cab_image_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.cab_image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cab_image_id_seq OWNER TO priyanka;

--
-- Name: cab_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.cab_image_id_seq OWNED BY public.cab_image.id;


--
-- Name: cab_invoice; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.cab_invoice (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    booking_id integer,
    slab integer,
    driver_night_allowance_charge numeric,
    car_night_allowance_charge numeric,
    total_hours integer,
    base_fare numeric,
    base_fare_weekend numeric,
    base_fare_peak_season numeric,
    base_fare_with_fuel numeric,
    different_pickup_drop_point_charge numeric,
    km_restriction numeric,
    fare_exceeded_per_hr numeric,
    fare_exceeded_per_km numeric,
    initial_km integer,
    initial_km_fare numeric,
    cancellation_charges numeric,
    distance numeric,
    total_fare numeric,
    website_id integer
);


ALTER TABLE public.cab_invoice OWNER TO priyanka;

--
-- Name: cab_invoice_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.cab_invoice_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cab_invoice_id_seq OWNER TO priyanka;

--
-- Name: cab_invoice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.cab_invoice_id_seq OWNED BY public.cab_invoice.id;


--
-- Name: cab_tax; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.cab_tax (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    invoice_id integer,
    gst numeric,
    s_gst numeric,
    c_gst numeric
);


ALTER TABLE public.cab_tax OWNER TO priyanka;

--
-- Name: cab_tax_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.cab_tax_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cab_tax_id_seq OWNER TO priyanka;

--
-- Name: cab_tax_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.cab_tax_id_seq OWNED BY public.cab_tax.id;


--
-- Name: cab_website; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.cab_website (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    website character varying,
    logo_image character varying
);


ALTER TABLE public.cab_website OWNER TO priyanka;

--
-- Name: cab_website_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.cab_website_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cab_website_id_seq OWNER TO priyanka;

--
-- Name: cab_website_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.cab_website_id_seq OWNED BY public.cab_website.id;


--
-- Name: collection; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.collection (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    collection character varying,
    image character varying
);


ALTER TABLE public.collection OWNER TO priyanka;

--
-- Name: collection_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.collection_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.collection_id_seq OWNER TO priyanka;

--
-- Name: collection_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.collection_id_seq OWNED BY public.collection.id;


--
-- Name: cuisine; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.cuisine (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    cuisine character varying
);


ALTER TABLE public.cuisine OWNER TO priyanka;

--
-- Name: cuisine_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.cuisine_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cuisine_id_seq OWNER TO priyanka;

--
-- Name: cuisine_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.cuisine_id_seq OWNED BY public.cuisine.id;


--
-- Name: deal; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.deal (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    price integer,
    hotel_url character varying,
    weekend boolean NOT NULL,
    website_id integer,
    room_id integer
);


ALTER TABLE public.deal OWNER TO priyanka;

--
-- Name: deal_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.deal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.deal_id_seq OWNER TO priyanka;

--
-- Name: deal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.deal_id_seq OWNED BY public.deal.id;


--
-- Name: dish; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.dish (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    restaurant_id integer,
    dish character varying,
    dish_type integer,
    half_price integer,
    full_price integer,
    "desc" text,
    image character varying
);


ALTER TABLE public.dish OWNER TO priyanka;

--
-- Name: dish_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.dish_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dish_id_seq OWNER TO priyanka;

--
-- Name: dish_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.dish_id_seq OWNED BY public.dish.id;


--
-- Name: facility; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.facility (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    bed_type integer,
    no_of_bed integer,
    bathroom_with_shower boolean,
    bathroom_nightie boolean,
    wardrobes_closet boolean,
    room_slipper boolean,
    morning_newspaper boolean,
    food_serve_at_room boolean,
    ironing_facility boolean,
    view boolean,
    free_toiletries boolean,
    bathroom_towels boolean,
    bathroom_cosmetics boolean,
    weighing_machine boolean,
    room_seating_area boolean,
    free_evening_snacks boolean,
    ac boolean,
    hairdryer boolean,
    wifi boolean,
    tv boolean,
    phone boolean,
    room_safe boolean,
    heater boolean,
    desk boolean,
    fan boolean,
    electric_kettle boolean,
    room_id integer
);


ALTER TABLE public.facility OWNER TO priyanka;

--
-- Name: facility_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.facility_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.facility_id_seq OWNER TO priyanka;

--
-- Name: facility_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.facility_id_seq OWNED BY public.facility.id;


--
-- Name: hotel; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.hotel (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    name character varying,
    star integer,
    rating numeric,
    phone character varying,
    city character varying,
    category character varying,
    "desc" text,
    address character varying,
    latitude double precision,
    longitude double precision
);


ALTER TABLE public.hotel OWNER TO priyanka;

--
-- Name: hotel_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.hotel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hotel_id_seq OWNER TO priyanka;

--
-- Name: hotel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.hotel_id_seq OWNED BY public.hotel.id;


--
-- Name: image; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.image (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    hotel_id integer,
    image_url character varying
);


ALTER TABLE public.image OWNER TO priyanka;

--
-- Name: image_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.image_id_seq OWNER TO priyanka;

--
-- Name: image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.image_id_seq OWNED BY public.image.id;


--
-- Name: member; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.member (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    no_of_adults integer,
    children integer,
    total_members integer,
    room_id integer
);


ALTER TABLE public.member OWNER TO priyanka;

--
-- Name: member_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.member_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.member_id_seq OWNER TO priyanka;

--
-- Name: member_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.member_id_seq OWNED BY public.member.id;


--
-- Name: menu; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.menu (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    restaurant_id integer,
    breakfast boolean,
    lunch boolean,
    dinner boolean,
    cafe boolean,
    lounge boolean,
    family boolean,
    bars boolean,
    nightlife boolean,
    street_stalls boolean,
    pocket_friendly boolean,
    diet boolean,
    luxury boolean
);


ALTER TABLE public.menu OWNER TO priyanka;

--
-- Name: menu_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.menu_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.menu_id_seq OWNER TO priyanka;

--
-- Name: menu_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.menu_id_seq OWNED BY public.menu.id;


--
-- Name: restaurant; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.restaurant (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    name character varying,
    rating numeric,
    price integer,
    "desc" text,
    city character varying,
    phone character varying,
    latitude double precision,
    longitude double precision,
    address character varying,
    category integer,
    featured boolean
);


ALTER TABLE public.restaurant OWNER TO priyanka;

--
-- Name: restaurant_amenity; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.restaurant_amenity (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    restaurant_id integer,
    home_delivery boolean,
    private_dining_area_available boolean,
    kid_friendly boolean,
    table_reservation_required boolean,
    table_booking_recommended boolean,
    wheelchair_accessible boolean,
    buffet boolean,
    wifi boolean,
    live_entertainment boolean,
    live_music boolean,
    live_sports_screening boolean,
    valet_parking boolean,
    parking boolean,
    group_meal boolean,
    smoking_area boolean,
    desserts_and_bakes boolean,
    full_bar_available boolean,
    serves_jain_food boolean,
    vegetarian_only boolean,
    serves_non_veg boolean,
    nightlife boolean,
    city_view boolean,
    brunch boolean,
    sunday_roast boolean,
    "gastro_Pub" boolean,
    beer boolean,
    outdoor_seating boolean,
    takeaway boolean,
    alcohol boolean,
    seating boolean
);


ALTER TABLE public.restaurant_amenity OWNER TO priyanka;

--
-- Name: restaurant_amenity_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.restaurant_amenity_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_amenity_id_seq OWNER TO priyanka;

--
-- Name: restaurant_amenity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.restaurant_amenity_id_seq OWNED BY public.restaurant_amenity.id;


--
-- Name: restaurant_association; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.restaurant_association (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    restaurant_id integer,
    collection_id integer,
    cuisine_id integer
);


ALTER TABLE public.restaurant_association OWNER TO priyanka;

--
-- Name: restaurant_association_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.restaurant_association_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_association_id_seq OWNER TO priyanka;

--
-- Name: restaurant_association_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.restaurant_association_id_seq OWNED BY public.restaurant_association.id;


--
-- Name: restaurant_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.restaurant_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_id_seq OWNER TO priyanka;

--
-- Name: restaurant_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.restaurant_id_seq OWNED BY public.restaurant.id;


--
-- Name: restaurant_image; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.restaurant_image (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    restaurant_id integer,
    image_url character varying,
    image_type integer
);


ALTER TABLE public.restaurant_image OWNER TO priyanka;

--
-- Name: restaurant_image_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.restaurant_image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.restaurant_image_id_seq OWNER TO priyanka;

--
-- Name: restaurant_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.restaurant_image_id_seq OWNED BY public.restaurant_image.id;


--
-- Name: room; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.room (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    hotel_id integer,
    status boolean,
    room_type integer,
    image_url character varying,
    other_room_type character varying,
    check_in timestamp with time zone NOT NULL,
    check_out timestamp with time zone NOT NULL,
    breakfast boolean,
    balcony boolean
);


ALTER TABLE public.room OWNER TO priyanka;

--
-- Name: room_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.room_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.room_id_seq OWNER TO priyanka;

--
-- Name: room_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.room_id_seq OWNED BY public.room.id;


--
-- Name: website; Type: TABLE; Schema: public; Owner: priyanka
--

CREATE TABLE public.website (
    id integer NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    website character varying,
    logo_image character varying
);


ALTER TABLE public.website OWNER TO priyanka;

--
-- Name: website_id_seq; Type: SEQUENCE; Schema: public; Owner: priyanka
--

CREATE SEQUENCE public.website_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.website_id_seq OWNER TO priyanka;

--
-- Name: website_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: priyanka
--

ALTER SEQUENCE public.website_id_seq OWNED BY public.website.id;


--
-- Name: amenity id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.amenity ALTER COLUMN id SET DEFAULT nextval('public.amenity_id_seq'::regclass);


--
-- Name: cab id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab ALTER COLUMN id SET DEFAULT nextval('public.cab_id_seq'::regclass);


--
-- Name: cab_amenity id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_amenity ALTER COLUMN id SET DEFAULT nextval('public.cab_amenity_id_seq'::regclass);


--
-- Name: cab_booking id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_booking ALTER COLUMN id SET DEFAULT nextval('public.cab_booking_id_seq'::regclass);


--
-- Name: cab_image id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_image ALTER COLUMN id SET DEFAULT nextval('public.cab_image_id_seq'::regclass);


--
-- Name: cab_invoice id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_invoice ALTER COLUMN id SET DEFAULT nextval('public.cab_invoice_id_seq'::regclass);


--
-- Name: cab_tax id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_tax ALTER COLUMN id SET DEFAULT nextval('public.cab_tax_id_seq'::regclass);


--
-- Name: cab_website id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_website ALTER COLUMN id SET DEFAULT nextval('public.cab_website_id_seq'::regclass);


--
-- Name: collection id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.collection ALTER COLUMN id SET DEFAULT nextval('public.collection_id_seq'::regclass);


--
-- Name: cuisine id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cuisine ALTER COLUMN id SET DEFAULT nextval('public.cuisine_id_seq'::regclass);


--
-- Name: deal id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.deal ALTER COLUMN id SET DEFAULT nextval('public.deal_id_seq'::regclass);


--
-- Name: dish id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.dish ALTER COLUMN id SET DEFAULT nextval('public.dish_id_seq'::regclass);


--
-- Name: facility id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.facility ALTER COLUMN id SET DEFAULT nextval('public.facility_id_seq'::regclass);


--
-- Name: hotel id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.hotel ALTER COLUMN id SET DEFAULT nextval('public.hotel_id_seq'::regclass);


--
-- Name: image id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.image ALTER COLUMN id SET DEFAULT nextval('public.image_id_seq'::regclass);


--
-- Name: member id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.member ALTER COLUMN id SET DEFAULT nextval('public.member_id_seq'::regclass);


--
-- Name: menu id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.menu ALTER COLUMN id SET DEFAULT nextval('public.menu_id_seq'::regclass);


--
-- Name: restaurant id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant ALTER COLUMN id SET DEFAULT nextval('public.restaurant_id_seq'::regclass);


--
-- Name: restaurant_amenity id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_amenity ALTER COLUMN id SET DEFAULT nextval('public.restaurant_amenity_id_seq'::regclass);


--
-- Name: restaurant_association id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_association ALTER COLUMN id SET DEFAULT nextval('public.restaurant_association_id_seq'::regclass);


--
-- Name: restaurant_image id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_image ALTER COLUMN id SET DEFAULT nextval('public.restaurant_image_id_seq'::regclass);


--
-- Name: room id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.room ALTER COLUMN id SET DEFAULT nextval('public.room_id_seq'::regclass);


--
-- Name: website id; Type: DEFAULT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.website ALTER COLUMN id SET DEFAULT nextval('public.website_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.alembic_version (version_num) FROM stdin;
7d58800f4200
\.


--
-- Data for Name: amenity; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.amenity (id, created_at, updated_at, hotel_id, conference_room, parking, couple_friendly, express_check_in_out, laundry_service, indoor_swimming_pool, outdoor_swimming_pool, porter_service, "Room_cleaning_service", terrace, child_baby_cot, wheelchair_accessible, doorman, hairdresser, banquets, non_smoking_smoking_rooms, pet_allowance, lift, bar, gym, pool, restaurant, spa, wifi_in_lobby, twenty_four_hr_reception, twenty_four_hr_room_service) FROM stdin;
\.


--
-- Data for Name: cab; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.cab (id, created_at, updated_at, car_name, city, car_type, cab_type, "desc") FROM stdin;
1	2018-07-29 12:27:50.552306+05:30	2018-07-29 12:27:50.552306+05:30	amaze	delhi	1	1	hjgyg
\.


--
-- Data for Name: cab_amenity; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.cab_amenity (id, created_at, updated_at, cab_id, air_condition, seater, baggage_allowance, doorstep_delivery, fuel, fuel_type, fuel_capacity, automatic, chauffeur, verified_driver) FROM stdin;
1	2018-07-29 12:28:49.207869+05:30	2018-07-29 12:28:49.207869+05:30	1	f	2	t	f	f	1	1	\N	\N	\N
\.


--
-- Data for Name: cab_booking; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.cab_booking (id, created_at, updated_at, cab_id, one_way, pickup_time, drop_time, outstation, drop_latitude, drop_longitude, pickup_latitude, pickup_longitude) FROM stdin;
1	2018-07-29 12:29:51.279726+05:30	2018-07-29 12:29:51.279726+05:30	1	f	2018-07-29 12:29:51.279726+05:30	2018-07-29 12:29:51.279726+05:30	f	2	2	2	2
\.


--
-- Data for Name: cab_image; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.cab_image (id, created_at, updated_at, cab_id, image_url) FROM stdin;
1	2018-07-29 12:30:22.335079+05:30	2018-07-29 12:30:22.335079+05:30	1	bgi
\.


--
-- Data for Name: cab_invoice; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.cab_invoice (id, created_at, updated_at, booking_id, slab, driver_night_allowance_charge, car_night_allowance_charge, total_hours, base_fare, base_fare_weekend, base_fare_peak_season, base_fare_with_fuel, different_pickup_drop_point_charge, km_restriction, fare_exceeded_per_hr, fare_exceeded_per_km, initial_km, initial_km_fare, cancellation_charges, distance, total_fare, website_id) FROM stdin;
1	2018-07-29 12:31:13.053769+05:30	2018-07-29 12:31:13.053769+05:30	1	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	2	1
\.


--
-- Data for Name: cab_tax; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.cab_tax (id, created_at, updated_at, invoice_id, gst, s_gst, c_gst) FROM stdin;
1	2018-07-29 12:31:43.544563+05:30	2018-07-29 12:31:43.544563+05:30	1	2	2	2
\.


--
-- Data for Name: cab_website; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.cab_website (id, created_at, updated_at, website, logo_image) FROM stdin;
1	\N	\N	gcfgdgcefgdfhv	cghscgdsfhvvh
\.


--
-- Data for Name: collection; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.collection (id, created_at, updated_at, collection, image) FROM stdin;
1	2018-07-18 18:13:53.524588+05:30	2018-07-18 18:13:53.524588+05:30	hbhjb	hjbhjb
\.


--
-- Data for Name: cuisine; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.cuisine (id, created_at, updated_at, cuisine) FROM stdin;
1	2018-07-18 18:13:27.660976+05:30	2018-07-18 18:13:27.660976+05:30	guuu
\.


--
-- Data for Name: deal; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.deal (id, created_at, updated_at, price, hotel_url, weekend, website_id, room_id) FROM stdin;
\.


--
-- Data for Name: dish; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.dish (id, created_at, updated_at, restaurant_id, dish, dish_type, half_price, full_price, "desc", image) FROM stdin;
1	2018-07-18 18:12:49.550956+05:30	2018-07-18 18:12:49.550956+05:30	\N	digi	\N	\N	\N	\N	uyg
\.


--
-- Data for Name: facility; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.facility (id, created_at, updated_at, bed_type, no_of_bed, bathroom_with_shower, bathroom_nightie, wardrobes_closet, room_slipper, morning_newspaper, food_serve_at_room, ironing_facility, view, free_toiletries, bathroom_towels, bathroom_cosmetics, weighing_machine, room_seating_area, free_evening_snacks, ac, hairdryer, wifi, tv, phone, room_safe, heater, desk, fan, electric_kettle, room_id) FROM stdin;
\.


--
-- Data for Name: hotel; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.hotel (id, created_at, updated_at, name, star, rating, phone, city, category, "desc", address, latitude, longitude) FROM stdin;
43	2018-07-18 17:56:25.902145+05:30	2018-07-18 17:56:25.902145+05:30	The Floatel	3	7.40000000000000036	\N	kolkata	luxury hotels	The Floatel is an eco-friendly property that is floating on the Hooghly River and is a five-minute walk from Millennium Park in the heart of Kolkata, India.  The hotel features 49 rooms, all of which include cable television, a safe, and a private bathroom with 24-hour running hot water. The hotel's suites come with a separate living room.  Amenities at the property include complimentary Wi-Fi, laundry services, on-site parking, and banquet facilities. The property has a swimming pool, fitness centre, and spa as well.  Breakfast is included in the cost of the room at The Floatel. The property has a multicuisine restaurant that is open 24 hours per day called The Bridge and a bar with an open terrace called The Anchorage.  The property is under 700 metres from Eden Gardens, a cricket ground built in the 19th century, and about one-and-a-half kilometres from a major shopping area called Satyanarayan Park A.C. Market.	9/10 Kolkata Jetty, Strand Road	88.3397482999999966	22.569901999999999
36	2018-07-18 14:06:50.93085+05:30	2018-07-18 14:35:50.862249+05:30	FabHotel Marble Arch	3	8.5	\N	delhi	premium hotel	Designed to meet the needs of business as well as leisure travelers, FabHotel Marble Arch offers simple rooms equipped with all essential amenities and backed by a team of professionals promising a hassle-free stay.  FabHotel Marble Arch, conveniently located on Pusa Lane, is one of the most preferred budget hotels in Karol Bagh. This budget hotel is in the vicinity of major city landmarks such as Sir Ganga Ram Hospital (240 m), Hanuman Mandir (550 m), Janki Devi Memorial College (550 m), Jhandewalan Devi Mandir (1.8 km), Connaught Place (3.2 km) and Talkatora Indoor Stadium (3.8 km).  All rooms at FabHotel Marble Arch are air-conditioned and come with television, tea/coffee maker and intercom. Private washrooms have a constant supply of hot/cold water and complimentary toiletries. Room service, front desk, round-the-clock security, power backup, and pick up and drop (on chargeable basis) are some of the additional facilities offered at this economy hotel in Karol Bagh.  Guests can relish mouth-watering dishes at the hotel’s restaurant. Alternatively, they can choose to dine out at the nearby restaurants and cafes like Karim’s, Art of Spices, Bikanervala Angan, Raffles Restaurant.	Plot No-8/6, W.E.A., Opposite Metro Pillar 88, Pusa Lane, Karol Bagh	77.1904332999999951	28.6451540000000016
37	2018-07-18 14:40:24.826083+05:30	2018-07-18 14:40:24.826083+05:30	Metro View	3	7.79999999999999982	\N	delhi	premium hotel	Hotel Metro View is situated right in the heart of New Delhi in Karol Bagh with shopping streets enveloping the property. We have a marvelous rooftop with refreshing views where you can either order a snack or a full meal from our in house Dine-In. Alternatively you may eat in the restaurant or order room service which is available 24-hours. High speed Wi-Fi & Internet connectivity throughout the property keeps you a step ahead always, not to mention that fast and seamless connectivity can help you do business, plan your trip, make necessary last minute adjustments, video chat with loved ones or simply entertain yourselves online.   Ours is a 3-star hotel which offers services and quality at prices unmatched, we strive hard to achieve levels of excellence which will bring you back to us time and again. The Hotel offers a environment which is friendly and we go the extra mile to let our guests feel fully comfortable and satisfied in serenity. Saying we are the quintessence of the 3-Star hospitality industry would not be an exaggeration.  The reception is open 24-hours to cater to your needs, we are at your service always!	17A/3, W.E.A., Karol Bagh	77.1873709999999988	28.6451020000000014
38	2018-07-18 15:06:21.410466+05:30	2018-07-18 15:06:21.410466+05:30	Golden Oasis	2	7	\N	delhi	premium hotels	Hotel Golden Oasis is located in Chandi Wali Street of Main Bazaar Road, Pahar Ganj. Situated just 5 minutes' walk away from New Delhi Railway Station and the nearest Metro Station, Hotel offers a distinguishing location advantage for all its guests. The hotel features 39 air-conditioned and well-ventilated guest rooms and hygienic bathrooms that combine comfort, style, elegance and the latest technology. These details along with its central location near Connaught Place & Railway Station make Golden Oasis an ideal place; both for leisure and business travelers.	901 Chandi Wali Street, Main Bazaar Road, Pahar Ganj	77.2126604000000043	28.6418169999999996
39	2018-07-18 15:34:06.742352+05:30	2018-07-18 15:34:06.742352+05:30	FabHotel Ascot	3	8.19999999999999929	\N	mumbai	premium hotel	Located near Mumbai Airport, FabHotel Ascot International provides the most affordable accommodation for frequent flyers and corporate travelers. FabHotel Ascot International is a budget hotel situated on Andheri Kurla Road in the Sakinaka locality of Andheri East. It is mostly preferred by business travelers due to its close proximity to several commercial complexes and industrial estates.Prominent landmarks near the hotel include Crescent Business Park (550 m), Logitech Park (700 m), Excom House (700 m), Accenture (800 m), Akruti Orchid Park (900 m), Times Square (950 m), Hyde Park (1.2 km), Prime Corporate Park (2.3 km), Ansa Industrial Estate (2.9 km), Powai (3.7 km), TCS (3.9 km), Neelkanth Business Park (4 km), SEEPZ (4.2 km), Deloitte (4.6 km), Nomura (4.7 km), and IIT (5.7 km). Easy accessibility from these landmarks makes the hotel one of the preferred budget hotels in Mumbai.Guests can consult doctors at Paramount Hospital, Axon Hospital and Seven Hills Hospital in case any medical assistance is required. For shopping and entertainment purposes, guests can head to Fashion Street (1 km) and Carnival BIG Cinemas Sangam.	3rd Floor, DilKap Center, Andheri Kurla Road	72.8828735999999964	19.1013407000000015
40	2018-07-18 16:01:03.029465+05:30	2018-07-18 16:20:44.42664+05:30	Kohinoor Continental	4	7.90000000000000036	\N	mumbai	premium hotels	Kohinoor Continental is conveniently located in the commercial hub of Mumbai on Andheri-Kurla Road.The is located 2KMS from Mumbai International Airport( CSIA). There is a total of 137 elegantly designed rooms classified into 118 Superior Rooms, 17 Premium Rooms and 2 Suites with contemporary chic decor and soft lighting. The basic room amenities offered by Hotel Kohinoor Continental includes flat screen TV, separate sitting area, mini bar, in-room safe, stationary kit, tea/coffee maker, iron, ironing board, Wi-Fi connectivity and individually controlled air-conditioning.There is a fitness centreas well as an outdoor swimming pool for those who want to maintain their fitness regime while travelling. An art gallery, travel desk, doctor on call, airport transfers and event spaces are other hotel facilities. The Solitaire is a multi-cuisine specialty restaurant. There isa coffee shop as well as The Beryl Club, the exclusive bar in the hotel where the guests can enjoy a drink and finger food.	International Airport Zone, Andheri Kurla Road, Andheri East	72.8657666000000006	19.1122730999999995
41	2018-07-18 16:28:03.366089+05:30	2018-07-18 16:28:03.366089+05:30	FabHotel Hyson	3	8.69999999999999929	\N	mumbai	premium hotel	With its warm hospitality, personalized services and sophisticated ambience, FabHotel Hyson International never fails to please guests. FabHotel Hyson International is strategically located at Mahakali Caves Road and is one of the best budget hotels in Mumbai due to its proximity to various corporate offices, commercial complexes, and tourist attractions. Patrons can enjoy a pleasant stay at this hotel with a wide range of modern facilities, including complimentary breakfast and Wi-Fi. Room service, 24-hour front desk, elevator, parking, round-the-clock security and doctor-on-call are the other conveniences offered here that make for a comfortable stay.  For accommodation, the hotel features capacious and spotlessly clean rooms equipped with various amenities such as AC, television, mini bar and tea/coffee maker. Attached bathrooms come with towels and complimentary toiletries.  Unmatched hospitality together with modern amenities is what defines this budget hotel in Mumbai. Each room in FabHotel Hyson International is provided with a wide menu of food from which guests can place an order as per their choice.	201/202 Brahans Business Park, 16 - A Mahal Estate	72.8605689999999981	19.1223495999999997
44	2018-07-18 18:19:40.502843+05:30	2018-07-18 18:19:40.502843+05:30	Greens Residency	2	7.59999999999999964	\N	bengaluru	premium hotels	Greens Residency located at No 118, Nawab Hyderali Khan Road, Ayyappa Temple	No 118, Nawab Hyderali Khan Road, Ayyappa Temple	77.5755259000000024	12.9595500000000001
42	2018-07-18 17:08:25.537485+05:30	2018-07-18 17:08:25.537485+05:30	The Peerless Inn	5	7.59999999999999964	\N	kolkata	luxury hotels	The Peerless Inn Kolkata is centrally located in the Chowringhee district of Kolkata. It features 168 rooms and suites and is just a short stroll from Esplanade Metro station and the delightful Maidan park.  The rooms, decorated with soothing earth colours, provide a king-size or two single beds, and a private bathroom with a shower and bath. Creature comforts include a television, a minibar and a tea/coffee maker.  The hotel’s conference and banqueting facilities can accommodate up to 350 attendees. A fitness centre is also available and Wi-Fi access is provided throughout the hotel.  The Peerless Inn Kolkata offers a good choice of on-site eateries: Aaheli serves tasty Bengali cuisine and Oceanic is the destination for seafood. The Tea Lounge features gourmet cakes and Ego is home to retro Asian dishes.  Both in Maidan park and within a mile and a half, Eden Gardens is where guests enjoy watching the Indian national team play cricket and Victoria Memorial Hall is a beautiful tribute to Queen Victoria.	12, J.l. Nehru Road	88.3492066999999963	22.5625408999999983
\.


--
-- Data for Name: image; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.image (id, created_at, updated_at, hotel_id, image_url) FROM stdin;
164	2018-07-18 14:06:50.971606+05:30	2018-07-18 14:06:50.971606+05:30	36	https://imgio.trivago.com/uploadimages/32/98/32985354_x.jpeg
165	2018-07-18 14:06:50.976993+05:30	2018-07-18 14:06:50.976993+05:30	36	https://imgio.trivago.com/uploadimages/32/98/32985358_x.jpeg
166	2018-07-18 14:06:50.981013+05:30	2018-07-18 14:06:50.981013+05:30	36	https://imgio.trivago.com/uploadimages/32/98/32985374_x.jpeg
167	2018-07-18 14:40:24.865111+05:30	2018-07-18 14:40:24.865111+05:30	37	https://imgio.trivago.com/partnerimages/14/35/143556886_x.jpeg
168	2018-07-18 14:40:24.870078+05:30	2018-07-18 14:40:24.870078+05:30	37	https://imgio.trivago.com/uploadimages/22/03/22038796_x.jpeg
169	2018-07-18 14:40:24.874833+05:30	2018-07-18 14:40:24.874833+05:30	37	https://imgio.trivago.com/partnerimages/14/35/143556916_x.jpeg
170	2018-07-18 15:06:21.437416+05:30	2018-07-18 15:06:21.437416+05:30	38	https://imgio.trivago.com/partnerimages/28/65/286549466_l.jpeg
171	2018-07-18 15:06:21.440988+05:30	2018-07-18 15:06:21.440988+05:30	38	https://imgio.trivago.com/uploadimages/26/26/26261124_l.jpeg
172	2018-07-18 15:06:21.444386+05:30	2018-07-18 15:06:21.444386+05:30	38	https://imgio.trivago.com/partnerimages/28/65/286549450_l.jpeg
173	2018-07-18 15:34:06.784422+05:30	2018-07-18 15:34:06.784422+05:30	39	https://imgio.trivago.com/uploadimages/28/26/28265334_x.jpeg
174	2018-07-18 15:34:06.789634+05:30	2018-07-18 15:34:06.789634+05:30	39	https://imgio.trivago.com/uploadimages/28/26/28265274_x.jpeg
175	2018-07-18 15:34:06.79489+05:30	2018-07-18 15:34:06.79489+05:30	39	https://imgio.trivago.com/uploadimages/28/26/28265256_x.jpeg
176	2018-07-18 15:34:06.799968+05:30	2018-07-18 15:34:06.799968+05:30	39	https://lh5.googleusercontent.com/p/AF1QipOXqxz1jHiQNm1RXixRhAdIT2GjHxZG2chdhrD_=w408-h314-k-no
177	2018-07-18 16:01:03.067481+05:30	2018-07-18 16:01:03.067481+05:30	40	https://imgio.trivago.com/partnerimages/10/21/102169376_x.jpeg
178	2018-07-18 16:01:03.071138+05:30	2018-07-18 16:01:03.071138+05:30	40	https://imgio.trivago.com/partnerimages/11/01/110117900_x.jpeg
179	2018-07-18 16:01:03.075903+05:30	2018-07-18 16:01:03.075903+05:30	40	https://imgio.trivago.com/partnerimages/11/01/110117902_x.jpeg
180	2018-07-18 16:01:03.080765+05:30	2018-07-18 16:01:03.080765+05:30	40	https://imgio.trivago.com/partnerimages/12/16/121698242_x.jpeg
181	2018-07-18 16:28:03.408483+05:30	2018-07-18 16:28:03.408483+05:30	41	https://imgio.trivago.com/uploadimages/28/26/28267870_x.jpeg
182	2018-07-18 16:28:03.413542+05:30	2018-07-18 16:28:03.413542+05:30	41	https://imgio.trivago.com/uploadimages/28/26/28267878_x.jpeg
183	2018-07-18 16:28:03.41831+05:30	2018-07-18 16:28:03.41831+05:30	41	https://imgio.trivago.com/uploadimages/28/26/28267900_x.jpeg
184	2018-07-18 16:28:03.423589+05:30	2018-07-18 16:28:03.423589+05:30	41	https://imgio.trivago.com/uploadimages/28/26/28267894_x.jpeg
185	2018-07-18 17:08:25.576415+05:30	2018-07-18 17:08:25.576415+05:30	42	https://imgio.trivago.com/partnerimages/17/79/177970498_x.jpeg
186	2018-07-18 17:08:25.579213+05:30	2018-07-18 17:08:25.579213+05:30	42	https://imgio.trivago.com/partnerimages/17/79/177970508_x.jpeg
187	2018-07-18 17:08:25.581903+05:30	2018-07-18 17:08:25.581903+05:30	42	https://imgio.trivago.com/partnerimages/17/79/177970542_x.jpeg
188	2018-07-18 17:56:25.943945+05:30	2018-07-18 17:56:25.943945+05:30	43	https://imgio.trivago.com/partnerimages/13/91/139119462_x.jpeg
189	2018-07-18 17:56:25.948635+05:30	2018-07-18 17:56:25.948635+05:30	43	https://imgio.trivago.com/partnerimages/13/91/139119466_x.jpeg
190	2018-07-18 17:56:25.953604+05:30	2018-07-18 17:56:25.953604+05:30	43	https://imgio.trivago.com/partnerimages/13/91/139119446_x.jpeg
191	2018-07-18 18:19:40.533027+05:30	2018-07-18 18:19:40.533027+05:30	44	https://imgio.trivago.com/itemimages/45/63/4563874_isq.jpeg
\.


--
-- Data for Name: member; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.member (id, created_at, updated_at, no_of_adults, children, total_members, room_id) FROM stdin;
\.


--
-- Data for Name: menu; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.menu (id, created_at, updated_at, restaurant_id, breakfast, lunch, dinner, cafe, lounge, family, bars, nightlife, street_stalls, pocket_friendly, diet, luxury) FROM stdin;
\.


--
-- Data for Name: restaurant; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.restaurant (id, created_at, updated_at, name, rating, price, "desc", city, phone, latitude, longitude, address, category, featured) FROM stdin;
1	2018-07-18 18:07:02.232656+05:30	2018-07-18 18:07:02.232656+05:30	res	2	\N	du	delhi	9897888888	2	2	vggug	2	f
\.


--
-- Data for Name: restaurant_amenity; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.restaurant_amenity (id, created_at, updated_at, restaurant_id, home_delivery, private_dining_area_available, kid_friendly, table_reservation_required, table_booking_recommended, wheelchair_accessible, buffet, wifi, live_entertainment, live_music, live_sports_screening, valet_parking, parking, group_meal, smoking_area, desserts_and_bakes, full_bar_available, serves_jain_food, vegetarian_only, serves_non_veg, nightlife, city_view, brunch, sunday_roast, "gastro_Pub", beer, outdoor_seating, takeaway, alcohol, seating) FROM stdin;
1	2018-07-18 18:11:03.700347+05:30	2018-07-18 18:11:03.700347+05:30	1	f	f	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
\.


--
-- Data for Name: restaurant_association; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.restaurant_association (id, created_at, updated_at, restaurant_id, collection_id, cuisine_id) FROM stdin;
\.


--
-- Data for Name: restaurant_image; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.restaurant_image (id, created_at, updated_at, restaurant_id, image_url, image_type) FROM stdin;
1	2018-07-18 18:11:53.040325+05:30	2018-07-18 18:11:53.040325+05:30	1	hiu	2
\.


--
-- Data for Name: room; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.room (id, created_at, updated_at, hotel_id, status, room_type, image_url, other_room_type, check_in, check_out, breakfast, balcony) FROM stdin;
37	2018-07-18 15:16:51.595483+05:30	2018-07-18 15:16:51.595483+05:30	38	t	1	https://images.trvl-media.com/hotels/21000000/20970000/20969800/20969706/cf643fec_z.jpg	DELUXE ROOM	2018-07-18 15:16:51.592495+05:30	2018-07-18 15:16:51.592513+05:30	t	f
39	2018-07-18 15:40:32.829217+05:30	2018-07-18 15:40:32.829217+05:30	39	t	1	https://t-ec.bstatic.com/xdata/images/hotel/square200/86275699.jpg?k=9223be4c4b015151e58d4a34519c15a102c281d4ba3e973cb2b4bd9f03648a6a&o=	Deluxe Room	2018-07-18 15:40:32.826453+05:30	2018-07-18 15:40:32.826479+05:30	t	f
40	2018-07-18 15:42:08.671829+05:30	2018-07-18 15:42:08.671829+05:30	39	t	1	https://t-ec.bstatic.com/xdata/images/hotel/square200/86275699.jpg?k=9223be4c4b015151e58d4a34519c15a102c281d4ba3e973cb2b4bd9f03648a6a&o=	Deluxe Room	2018-07-18 15:42:08.670109+05:30	2018-07-18 15:42:08.670122+05:30	t	f
42	2018-07-18 16:34:31.410255+05:30	2018-07-18 16:34:31.410255+05:30	41	t	2	https://images.trvl-media.com/hotels/20000000/19080000/19072200/19072151/ad62c4ee_l.jpg	Executive Room	2018-07-18 16:34:31.407966+05:30	2018-07-18 16:34:31.407993+05:30	t	f
43	2018-07-18 17:10:59.890234+05:30	2018-07-18 17:10:59.890234+05:30	42	t	1	https://r1imghtlak.mmtcdn.com/l9of9o0p5p1018pc0s21k8fi000p.jpg?&downsize=800:*&crop=800:490;0,19&output-format=jpg	Superior Room	2018-07-18 17:10:59.886951+05:30	2018-07-18 17:10:59.886972+05:30	f	f
44	2018-07-18 17:12:33.422654+05:30	2018-07-18 17:12:33.422654+05:30	42	t	2	https://r1imghtlak.mmtcdn.com/8b0b0624377111e5b1b3001ec9b85d13.jfif?&downsize=800:*&crop=800:490;0,24&output-format=jpg	Premier Room	2018-07-18 17:12:33.418789+05:30	2018-07-18 17:12:33.418811+05:30	t	f
45	2018-07-18 17:14:05.00084+05:30	2018-07-18 17:14:05.00084+05:30	42	t	3	https://r1imghtlak.mmtcdn.com/6j0p0r0av90q70rahanc48gn005c.jpg?&downsize=800:*&crop=800:490;0,19&output-format=jpg	Suite	2018-07-18 17:14:04.998918+05:30	2018-07-18 17:14:04.998932+05:30	t	f
46	2018-07-18 17:18:40.254103+05:30	2018-07-18 17:18:40.254103+05:30	42	t	1	https://images.trvl-media.com/hotels/2000000/1070000/1066400/1066383/1066383_55_l.jpg	Superior Room	2018-07-18 17:18:40.251896+05:30	2018-07-18 17:18:40.251927+05:30	t	f
36	2018-07-18 15:13:00.269366+05:30	2018-07-18 15:13:00.269366+05:30	38	t	1	https://r1imghtlak.mmtcdn.com/ee1db456b0a411e7905c0a209fbd0127.jpg?&downsize=800:*&crop=800:490;0,21&output-format=jpg	DELUXE ROOM	2018-07-18 15:13:00.261064+05:30	2018-07-18 15:13:00.261083+05:30	f	f
38	2018-07-18 15:38:15.161643+05:30	2018-07-18 15:38:15.161643+05:30	39	t	1	https://t-ec.bstatic.com/xdata/images/hotel/square200/86275699.jpg?k=9223be4c4b015151e58d4a34519c15a102c281d4ba3e973cb2b4bd9f03648a6a&o=	Deluxe Room	2018-07-18 15:38:15.158797+05:30	2018-07-18 15:38:15.158819+05:30	f	f
41	2018-07-18 16:31:41.425607+05:30	2018-07-18 16:31:41.425607+05:30	41	t	1	https://images.trvl-media.com/hotels/20000000/19080000/19072200/19072151/ad62c4ee_l.jpg	Deluxe Room	2018-07-18 16:31:41.42345+05:30	2018-07-18 16:31:41.423459+05:30	f	f
47	2018-07-18 17:58:06.330647+05:30	2018-07-18 17:58:06.330647+05:30	43	t	1	https://r1imghtlak.mmtcdn.com/gc29knnm4l65v1edfsikbf9i0040.jpg?&downsize=800:*&crop=800:490;0,19&output-format=jpg	Sunrise	2018-07-18 17:58:06.329466+05:30	2018-07-18 17:58:06.329476+05:30	f	f
\.


--
-- Data for Name: website; Type: TABLE DATA; Schema: public; Owner: priyanka
--

COPY public.website (id, created_at, updated_at, website, logo_image) FROM stdin;
54	2018-07-14 12:41:30.589798+05:30	2018-07-14 12:41:30.589798+05:30	agoda	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36931403_216842772279716_2011806305429225472_n.png?_nc_cat=0&oh=5c6993b4473bfe525b213139fbd23385&oe=5BA3054D
55	2018-07-14 12:41:30.593878+05:30	2018-07-14 12:41:30.593878+05:30	airbnb	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36931403_216842772279716_2011806305429225472_n.png?_nc_cat=0&oh=5c6993b4473bfe525b213139fbd23385&oe=5BA3054D
56	2018-07-14 12:41:30.596076+05:30	2018-07-14 12:41:30.596076+05:30	amoma	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36931403_216842772279716_2011806305429225472_n.png?_nc_cat=0&oh=5c6993b4473bfe525b213139fbd23385&oe=5BA3054D
57	2018-07-14 12:41:30.598265+05:30	2018-07-14 12:41:30.598265+05:30	booking	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36915080_216842838946376_330549487783116800_n.png?_nc_cat=0&oh=6e958718ed11a123b197c3193dc05aed&oe=5BDD448D
58	2018-07-14 12:41:30.600185+05:30	2018-07-14 12:41:30.600185+05:30	booking-buddy	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36985547_216842062279787_7777784442721927168_n.png?_nc_cat=0&oh=e5c62603447fe0fbe146e13bd4de9457&oe=5BDC1466
59	2018-07-14 12:41:30.602272+05:30	2018-07-14 12:41:30.602272+05:30	cheapoair	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36871613_216843158946344_3551985700943429632_n.png?_nc_cat=0&oh=a5a158f31d8d1f012741dd93ecb3aaea&oe=5BE8B42F
60	2018-07-14 12:41:30.605512+05:30	2018-07-14 12:41:30.605512+05:30	clear-trip	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36871613_216843158946344_3551985700943429632_n.png?_nc_cat=0&oh=a5a158f31d8d1f012741dd93ecb3aaea&oe=5BE8B42F
61	2018-07-14 12:41:30.610011+05:30	2018-07-14 12:41:30.610011+05:30	cheap-tickets	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36919085_216843172279676_6441419649337786368_n.png?_nc_cat=0&oh=e42a76953178b4337800da6b67186584&oe=5B9EAEFC
62	2018-07-14 12:41:30.61466+05:30	2018-07-14 12:41:30.61466+05:30	easy-my-trip	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36866925_216842065613120_2808019613483270144_n.png?_nc_cat=0&oh=907872891a881a793944fd09f4961ed4&oe=5BD912D7
63	2018-07-14 12:41:30.61989+05:30	2018-07-14 12:41:30.61989+05:30	elvoline	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36878591_216842138946446_5193606172380233728_n.png?_nc_cat=0&oh=0ad29a61d7053926027e721d68debc23&oe=5BDD9351
64	2018-07-14 12:41:30.624777+05:30	2018-07-14 12:41:30.624777+05:30	expedia	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36940748_216842142279779_153710806440083456_n.png?_nc_cat=0&oh=2d914f9db4369665fb9cf387084994af&oe=5BD4EF3F
65	2018-07-14 12:41:30.63001+05:30	2018-07-14 12:41:30.63001+05:30	fab-hotels	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36940748_216842142279779_153710806440083456_n.png?_nc_cat=0&oh=2d914f9db4369665fb9cf387084994af&oe=5BD4EF3F
66	2018-07-14 12:41:30.634822+05:30	2018-07-14 12:41:30.634822+05:30	fairmont	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36940748_216842142279779_153710806440083456_n.png?_nc_cat=0&oh=2d914f9db4369665fb9cf387084994af&oe=5BD4EF3F
67	2018-07-14 12:41:30.63956+05:30	2018-07-14 12:41:30.63956+05:30	go-ibibo	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36940748_216842142279779_153710806440083456_n.png?_nc_cat=0&oh=2d914f9db4369665fb9cf387084994af&oe=5BD4EF3F
68	2018-07-14 12:41:30.644219+05:30	2018-07-14 12:41:30.644219+05:30	hilton	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36940748_216842142279779_153710806440083456_n.png?_nc_cat=0&oh=2d914f9db4369665fb9cf387084994af&oe=5BD4EF3F
69	2018-07-14 12:41:30.648944+05:30	2018-07-14 12:41:30.648944+05:30	home-away	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36940748_216842142279779_153710806440083456_n.png?_nc_cat=0&oh=2d914f9db4369665fb9cf387084994af&oe=5BD4EF3F
70	2018-07-14 12:41:30.6537+05:30	2018-07-14 12:41:30.6537+05:30	home-stay	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36940748_216842142279779_153710806440083456_n.png?_nc_cat=0&oh=2d914f9db4369665fb9cf387084994af&oe=5BD4EF3F
71	2018-07-14 12:41:30.658362+05:30	2018-07-14 12:41:30.658362+05:30	hostels	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36940748_216842142279779_153710806440083456_n.png?_nc_cat=0&oh=2d914f9db4369665fb9cf387084994af&oe=5BD4EF3F
72	2018-07-14 12:41:30.663002+05:30	2018-07-14 12:41:30.663002+05:30	hostelworld-logo.png1	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36899985_216842212279772_2750645301449588736_n.png?_nc_cat=0&oh=03ca6dceb21820dd5036d8da74b53115&oe=5BDD5EEE
73	2018-07-14 12:41:30.66771+05:30	2018-07-14 12:41:30.66771+05:30	hotel-info	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36870947_216842748946385_164330100194541568_n.png?_nc_cat=0&oh=ef56567fccea5123616fdf7a00ec6312&oe=5B9F854C
74	2018-07-14 12:41:30.672429+05:30	2018-07-14 12:41:30.672429+05:30	hotel-planner	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36867574_216842985613028_6293552927587958784_n.png?_nc_cat=0&oh=2a0a5e5b52beeaba12dbd624a22a916e&oe=5BE85D64
75	2018-07-14 12:41:30.677471+05:30	2018-07-14 12:41:30.677471+05:30	hotel-quickly	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36867574_216842985613028_6293552927587958784_n.png?_nc_cat=0&oh=2a0a5e5b52beeaba12dbd624a22a916e&oe=5BE85D64
76	2018-07-14 12:41:30.682523+05:30	2018-07-14 12:41:30.682523+05:30	hotels	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36867574_216842985613028_6293552927587958784_n.png?_nc_cat=0&oh=2a0a5e5b52beeaba12dbd624a22a916e&oe=5BE85D64
77	2018-07-14 12:41:30.687318+05:30	2018-07-14 12:41:30.687318+05:30	hotels-combined	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36867574_216842985613028_6293552927587958784_n.png?_nc_cat=0&oh=2a0a5e5b52beeaba12dbd624a22a916e&oe=5BE85D64
78	2018-07-14 12:41:30.691971+05:30	2018-07-14 12:41:30.691971+05:30	hotel-urbano	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36867574_216842985613028_6293552927587958784_n.png?_nc_cat=0&oh=2a0a5e5b52beeaba12dbd624a22a916e&oe=5BE85D64
79	2018-07-14 12:41:30.696612+05:30	2018-07-14 12:41:30.696612+05:30	hotwire	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36867574_216842985613028_6293552927587958784_n.png?_nc_cat=0&oh=2a0a5e5b52beeaba12dbd624a22a916e&oe=5BE85D64
80	2018-07-14 12:41:30.701285+05:30	2018-07-14 12:41:30.701285+05:30	hyatt	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36878589_216842238946436_2729499480939298816_n.png?_nc_cat=0&oh=99feacf6a4ea29000fb95906fb13c95e&oe=5BA74A18
81	2018-07-14 12:41:30.705812+05:30	2018-07-14 12:41:30.705812+05:30	ibis-hotels	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36878589_216842238946436_2729499480939298816_n.png?_nc_cat=0&oh=99feacf6a4ea29000fb95906fb13c95e&oe=5BA74A18
82	2018-07-14 12:41:30.70962+05:30	2018-07-14 12:41:30.70962+05:30	intercontinental	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36878589_216842238946436_2729499480939298816_n.png?_nc_cat=0&oh=99feacf6a4ea29000fb95906fb13c95e&oe=5BA74A18
83	2018-07-14 12:41:30.712615+05:30	2018-07-14 12:41:30.712615+05:30	kayak	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36869923_216842318946428_6939867771022868480_n.png?_nc_cat=0&oh=7f623ada5716fede3632c3324c2041b3&oe=5BD8E2B3
84	2018-07-14 12:41:30.715452+05:30	2018-07-14 12:41:30.715452+05:30	lonely-planet	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36869923_216842318946428_6939867771022868480_n.png?_nc_cat=0&oh=7f623ada5716fede3632c3324c2041b3&oe=5BD8E2B3
85	2018-07-14 12:41:30.718256+05:30	2018-07-14 12:41:30.718256+05:30	make-my-trip	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/37023397_216842328946427_1052161928324972544_n.png?_nc_cat=0&oh=77b905bb14d44c4c9c3539229f8aa6c2&oe=5BCEED6C
86	2018-07-14 12:41:30.721185+05:30	2018-07-14 12:41:30.721185+05:30	melia	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/37023397_216842328946427_1052161928324972544_n.png?_nc_cat=0&oh=77b905bb14d44c4c9c3539229f8aa6c2&oe=5BCEED6C
87	2018-07-14 12:41:30.724143+05:30	2018-07-14 12:41:30.724143+05:30	novotel	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/37005247_216842342279759_5367885005970210816_n.png?_nc_cat=0&oh=50a287ce76f960fe92ffe1b5b273edd0&oe=5BD21F95
88	2018-07-14 12:41:30.727132+05:30	2018-07-14 12:41:30.727132+05:30	one-travel	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36887858_216842365613090_7991306237876633600_n.png?_nc_cat=0&oh=560188c14578da6d07bf7fcc828289cc&oe=5BA5253E
89	2018-07-14 12:41:30.730124+05:30	2018-07-14 12:41:30.730124+05:30	orbtiz	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36887858_216842365613090_7991306237876633600_n.png?_nc_cat=0&oh=560188c14578da6d07bf7fcc828289cc&oe=5BA5253E
90	2018-07-14 12:41:30.732963+05:30	2018-07-14 12:41:30.732963+05:30	otel	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36887858_216842365613090_7991306237876633600_n.png?_nc_cat=0&oh=560188c14578da6d07bf7fcc828289cc&oe=5BA5253E
91	2018-07-14 12:41:30.735887+05:30	2018-07-14 12:41:30.735887+05:30	priceline	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36869685_216842775613049_4132134438584713216_n.png?_nc_cat=0&oh=73720197caf7900daa7774dd29ac28e8&oe=5BA3BE33
92	2018-07-14 12:41:30.739581+05:30	2018-07-14 12:41:30.739581+05:30	rakuten	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36907538_216842725613054_2166548934812499968_n.png?_nc_cat=0&oh=32ccaa6f3e3099ec5b60120ae801846d&oe=5BEA706A
93	2018-07-14 12:41:30.744249+05:30	2018-07-14 12:41:30.744249+05:30	sky-scanner	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36907538_216842725613054_2166548934812499968_n.png?_nc_cat=0&oh=32ccaa6f3e3099ec5b60120ae801846d&oe=5BEA706A
94	2018-07-14 12:41:30.748813+05:30	2018-07-14 12:41:30.748813+05:30	roomer	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36972856_216842428946417_5190496697662308352_n.png?_nc_cat=0&oh=c2969c686acfd0d390867e235258a900&oe=5BEC770B
95	2018-07-14 12:41:30.753554+05:30	2018-07-14 12:41:30.753554+05:30	sponsor-jahan	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36975137_216843045613022_5619564647792246784_n.png?_nc_cat=0&oh=0b3d28dac37e5eea2a50aef5fd980530&oe=5BE7AE6E
96	2018-07-14 12:41:30.758219+05:30	2018-07-14 12:41:30.758219+05:30	sofitel	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36975886_216842452279748_312970517353070592_n.png?_nc_cat=0&oh=0c34177256009ad16428986987fc4638&oe=5BD4E59C
97	2018-07-14 12:41:30.762809+05:30	2018-07-14 12:41:30.762809+05:30	travel-guru	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36869916_216843252279668_4520049854625349632_n.png?_nc_cat=0&oh=75ca1555064c529a630f558de956d638&oe=5BDA75BB
98	2018-07-14 12:41:30.767363+05:30	2018-07-14 12:41:30.767363+05:30	travelo-city	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36846166_216842948946365_4734756115860946944_n.png?_nc_cat=0&oh=70599f3814be48364de1d9caa46b32b1&oe=5BD838DB
99	2018-07-14 12:41:30.771944+05:30	2018-07-14 12:41:30.771944+05:30	travel-zoo	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36846166_216842948946365_4734756115860946944_n.png?_nc_cat=0&oh=70599f3814be48364de1d9caa46b32b1&oe=5BD838DB
100	2018-07-14 12:41:30.776524+05:30	2018-07-14 12:41:30.776524+05:30	treebo	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36846166_216842948946365_4734756115860946944_n.png?_nc_cat=0&oh=70599f3814be48364de1d9caa46b32b1&oe=5BD838DB
101	2018-07-14 12:41:30.781185+05:30	2018-07-14 12:41:30.781185+05:30	trip	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36846166_216842948946365_4734756115860946944_n.png?_nc_cat=0&oh=70599f3814be48364de1d9caa46b32b1&oe=5BD838DB
102	2018-07-14 12:41:30.78574+05:30	2018-07-14 12:41:30.78574+05:30	vrbo	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36846166_216842948946365_4734756115860946944_n.png?_nc_cat=0&oh=70599f3814be48364de1d9caa46b32b1&oe=5BD838DB
103	2018-07-14 12:41:30.790344+05:30	2018-07-14 12:41:30.790344+05:30	wego	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36872568_216842855613041_905143475501006848_n.png?_nc_cat=0&oh=930064d0f5028e54a0f864d9422eaa74&oe=5BD6130D
104	2018-07-14 12:41:30.794941+05:30	2018-07-14 12:41:30.794941+05:30	yatra	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36957657_216843235613003_2117808142698938368_n.png?_nc_cat=0&oh=670e16501a96d5e2fededdfc6aa28895&oe=5BE815F6
105	2018-07-14 12:41:30.799559+05:30	2018-07-14 12:41:30.799559+05:30	zen-hotels	https://scontent.fdel1-4.fna.fbcdn.net/v/t1.0-9/36957657_216843235613003_2117808142698938368_n.png?_nc_cat=0&oh=670e16501a96d5e2fededdfc6aa28895&oe=5BE815F6
\.


--
-- Name: amenity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.amenity_id_seq', 44, true);


--
-- Name: cab_amenity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.cab_amenity_id_seq', 1, false);


--
-- Name: cab_booking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.cab_booking_id_seq', 1, false);


--
-- Name: cab_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.cab_id_seq', 1, false);


--
-- Name: cab_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.cab_image_id_seq', 1, false);


--
-- Name: cab_invoice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.cab_invoice_id_seq', 1, false);


--
-- Name: cab_tax_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.cab_tax_id_seq', 1, false);


--
-- Name: cab_website_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.cab_website_id_seq', 1, true);


--
-- Name: collection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.collection_id_seq', 1, false);


--
-- Name: cuisine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.cuisine_id_seq', 1, false);


--
-- Name: deal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.deal_id_seq', 110, true);


--
-- Name: dish_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.dish_id_seq', 1, false);


--
-- Name: facility_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.facility_id_seq', 47, true);


--
-- Name: hotel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.hotel_id_seq', 44, true);


--
-- Name: image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.image_id_seq', 191, true);


--
-- Name: member_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.member_id_seq', 47, true);


--
-- Name: menu_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.menu_id_seq', 1, false);


--
-- Name: restaurant_amenity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.restaurant_amenity_id_seq', 1, false);


--
-- Name: restaurant_association_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.restaurant_association_id_seq', 1, false);


--
-- Name: restaurant_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.restaurant_id_seq', 1, false);


--
-- Name: restaurant_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.restaurant_image_id_seq', 1, false);


--
-- Name: room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.room_id_seq', 47, true);


--
-- Name: website_id_seq; Type: SEQUENCE SET; Schema: public; Owner: priyanka
--

SELECT pg_catalog.setval('public.website_id_seq', 105, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: amenity amenity_hotel_id_key; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.amenity
    ADD CONSTRAINT amenity_hotel_id_key UNIQUE (hotel_id);


--
-- Name: amenity amenity_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.amenity
    ADD CONSTRAINT amenity_pkey PRIMARY KEY (id);


--
-- Name: cab_amenity cab_amenity_cab_id_key; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_amenity
    ADD CONSTRAINT cab_amenity_cab_id_key UNIQUE (cab_id);


--
-- Name: cab_amenity cab_amenity_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_amenity
    ADD CONSTRAINT cab_amenity_pkey PRIMARY KEY (id);


--
-- Name: cab_booking cab_booking_cab_id_key; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_booking
    ADD CONSTRAINT cab_booking_cab_id_key UNIQUE (cab_id);


--
-- Name: cab_booking cab_booking_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_booking
    ADD CONSTRAINT cab_booking_pkey PRIMARY KEY (id);


--
-- Name: cab_image cab_image_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_image
    ADD CONSTRAINT cab_image_pkey PRIMARY KEY (id);


--
-- Name: cab_invoice cab_invoice_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_invoice
    ADD CONSTRAINT cab_invoice_pkey PRIMARY KEY (id);


--
-- Name: cab cab_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab
    ADD CONSTRAINT cab_pkey PRIMARY KEY (id);


--
-- Name: cab_tax cab_tax_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_tax
    ADD CONSTRAINT cab_tax_pkey PRIMARY KEY (id);


--
-- Name: cab_website cab_website_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_website
    ADD CONSTRAINT cab_website_pkey PRIMARY KEY (id);


--
-- Name: collection collection_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.collection
    ADD CONSTRAINT collection_pkey PRIMARY KEY (id);


--
-- Name: cuisine cuisine_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cuisine
    ADD CONSTRAINT cuisine_pkey PRIMARY KEY (id);


--
-- Name: deal deal_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.deal
    ADD CONSTRAINT deal_pkey PRIMARY KEY (id);


--
-- Name: dish dish_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.dish
    ADD CONSTRAINT dish_pkey PRIMARY KEY (id);


--
-- Name: facility facility_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.facility
    ADD CONSTRAINT facility_pkey PRIMARY KEY (id);


--
-- Name: facility facility_room_id_key; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.facility
    ADD CONSTRAINT facility_room_id_key UNIQUE (room_id);


--
-- Name: hotel hotel_phone_key; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.hotel
    ADD CONSTRAINT hotel_phone_key UNIQUE (phone);


--
-- Name: hotel hotel_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.hotel
    ADD CONSTRAINT hotel_pkey PRIMARY KEY (id);


--
-- Name: image image_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_pkey PRIMARY KEY (id);


--
-- Name: member member_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_pkey PRIMARY KEY (id);


--
-- Name: member member_room_id_key; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_room_id_key UNIQUE (room_id);


--
-- Name: menu menu_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.menu
    ADD CONSTRAINT menu_pkey PRIMARY KEY (id);


--
-- Name: menu menu_restaurant_id_key; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.menu
    ADD CONSTRAINT menu_restaurant_id_key UNIQUE (restaurant_id);


--
-- Name: restaurant_amenity restaurant_amenity_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_amenity
    ADD CONSTRAINT restaurant_amenity_pkey PRIMARY KEY (id);


--
-- Name: restaurant_amenity restaurant_amenity_restaurant_id_key; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_amenity
    ADD CONSTRAINT restaurant_amenity_restaurant_id_key UNIQUE (restaurant_id);


--
-- Name: restaurant_association restaurant_association_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_association
    ADD CONSTRAINT restaurant_association_pkey PRIMARY KEY (id);


--
-- Name: restaurant_image restaurant_image_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_image
    ADD CONSTRAINT restaurant_image_pkey PRIMARY KEY (id);


--
-- Name: restaurant restaurant_phone_key; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant
    ADD CONSTRAINT restaurant_phone_key UNIQUE (phone);


--
-- Name: restaurant restaurant_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant
    ADD CONSTRAINT restaurant_pkey PRIMARY KEY (id);


--
-- Name: room room_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_pkey PRIMARY KEY (id);


--
-- Name: website website_pkey; Type: CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.website
    ADD CONSTRAINT website_pkey PRIMARY KEY (id);


--
-- Name: ix_amenity_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_amenity_id ON public.amenity USING btree (id);


--
-- Name: ix_cab_amenity_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_cab_amenity_id ON public.cab_amenity USING btree (id);


--
-- Name: ix_cab_booking_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_cab_booking_id ON public.cab_booking USING btree (id);


--
-- Name: ix_cab_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_cab_id ON public.cab USING btree (id);


--
-- Name: ix_cab_image_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_cab_image_id ON public.cab_image USING btree (id);


--
-- Name: ix_cab_invoice_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_cab_invoice_id ON public.cab_invoice USING btree (id);


--
-- Name: ix_cab_tax_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_cab_tax_id ON public.cab_tax USING btree (id);


--
-- Name: ix_cab_website_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_cab_website_id ON public.cab_website USING btree (id);


--
-- Name: ix_collection_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_collection_id ON public.collection USING btree (id);


--
-- Name: ix_cuisine_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_cuisine_id ON public.cuisine USING btree (id);


--
-- Name: ix_deal_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_deal_id ON public.deal USING btree (id);


--
-- Name: ix_dish_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_dish_id ON public.dish USING btree (id);


--
-- Name: ix_facility_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_facility_id ON public.facility USING btree (id);


--
-- Name: ix_hotel_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_hotel_id ON public.hotel USING btree (id);


--
-- Name: ix_image_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_image_id ON public.image USING btree (id);


--
-- Name: ix_member_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_member_id ON public.member USING btree (id);


--
-- Name: ix_menu_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_menu_id ON public.menu USING btree (id);


--
-- Name: ix_restaurant_amenity_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_restaurant_amenity_id ON public.restaurant_amenity USING btree (id);


--
-- Name: ix_restaurant_association_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_restaurant_association_id ON public.restaurant_association USING btree (id);


--
-- Name: ix_restaurant_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_restaurant_id ON public.restaurant USING btree (id);


--
-- Name: ix_restaurant_image_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_restaurant_image_id ON public.restaurant_image USING btree (id);


--
-- Name: ix_room_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_room_id ON public.room USING btree (id);


--
-- Name: ix_website_id; Type: INDEX; Schema: public; Owner: priyanka
--

CREATE INDEX ix_website_id ON public.website USING btree (id);


--
-- Name: amenity amenity_hotel_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.amenity
    ADD CONSTRAINT amenity_hotel_id_fkey FOREIGN KEY (hotel_id) REFERENCES public.hotel(id);


--
-- Name: cab_amenity cab_amenity_cab_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_amenity
    ADD CONSTRAINT cab_amenity_cab_id_fkey FOREIGN KEY (cab_id) REFERENCES public.cab(id);


--
-- Name: cab_booking cab_booking_cab_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_booking
    ADD CONSTRAINT cab_booking_cab_id_fkey FOREIGN KEY (cab_id) REFERENCES public.cab(id);


--
-- Name: cab_image cab_image_cab_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_image
    ADD CONSTRAINT cab_image_cab_id_fkey FOREIGN KEY (cab_id) REFERENCES public.cab(id);


--
-- Name: cab_invoice cab_invoice_booking_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_invoice
    ADD CONSTRAINT cab_invoice_booking_id_fkey FOREIGN KEY (booking_id) REFERENCES public.cab_booking(id);


--
-- Name: cab_invoice cab_invoice_website_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_invoice
    ADD CONSTRAINT cab_invoice_website_id_fkey FOREIGN KEY (website_id) REFERENCES public.cab_website(id);


--
-- Name: cab_tax cab_tax_invoice_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.cab_tax
    ADD CONSTRAINT cab_tax_invoice_id_fkey FOREIGN KEY (invoice_id) REFERENCES public.cab_invoice(id);


--
-- Name: deal deal_room_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.deal
    ADD CONSTRAINT deal_room_id_fkey FOREIGN KEY (room_id) REFERENCES public.room(id);


--
-- Name: deal deal_website_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.deal
    ADD CONSTRAINT deal_website_id_fkey FOREIGN KEY (website_id) REFERENCES public.website(id);


--
-- Name: dish dish_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.dish
    ADD CONSTRAINT dish_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurant(id);


--
-- Name: facility facility_room_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.facility
    ADD CONSTRAINT facility_room_id_fkey FOREIGN KEY (room_id) REFERENCES public.room(id);


--
-- Name: image image_hotel_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.image
    ADD CONSTRAINT image_hotel_id_fkey FOREIGN KEY (hotel_id) REFERENCES public.hotel(id);


--
-- Name: member member_room_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_room_id_fkey FOREIGN KEY (room_id) REFERENCES public.room(id);


--
-- Name: menu menu_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.menu
    ADD CONSTRAINT menu_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurant(id);


--
-- Name: restaurant_amenity restaurant_amenity_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_amenity
    ADD CONSTRAINT restaurant_amenity_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurant(id);


--
-- Name: restaurant_association restaurant_association_collection_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_association
    ADD CONSTRAINT restaurant_association_collection_id_fkey FOREIGN KEY (collection_id) REFERENCES public.collection(id);


--
-- Name: restaurant_association restaurant_association_cuisine_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_association
    ADD CONSTRAINT restaurant_association_cuisine_id_fkey FOREIGN KEY (cuisine_id) REFERENCES public.cuisine(id);


--
-- Name: restaurant_association restaurant_association_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_association
    ADD CONSTRAINT restaurant_association_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurant(id);


--
-- Name: restaurant_image restaurant_image_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.restaurant_image
    ADD CONSTRAINT restaurant_image_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurant(id);


--
-- Name: room room_hotel_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: priyanka
--

ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_hotel_id_fkey FOREIGN KEY (hotel_id) REFERENCES public.hotel(id);


--
-- PostgreSQL database dump complete
--

