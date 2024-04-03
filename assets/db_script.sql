--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

-- Started on 2024-04-02 17:10:50

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 7 (class 2615 OID 17828)
-- Name: epic_events; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA epic_events;


ALTER SCHEMA epic_events OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 224 (class 1259 OID 18278)
-- Name: clients; Type: TABLE; Schema: epic_events; Owner: postgres
--

CREATE TABLE epic_events.clients (
    id integer NOT NULL,
    name_client character varying,
    email character varying,
    phone character varying,
    creation_date date,
    update_date date,
    company_id integer,
    commercial_id integer
);


ALTER TABLE epic_events.clients OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 18277)
-- Name: clients_id_seq; Type: SEQUENCE; Schema: epic_events; Owner: postgres
--

CREATE SEQUENCE epic_events.clients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE epic_events.clients_id_seq OWNER TO postgres;

--
-- TOC entry 4905 (class 0 OID 0)
-- Dependencies: 223
-- Name: clients_id_seq; Type: SEQUENCE OWNED BY; Schema: epic_events; Owner: postgres
--

ALTER SEQUENCE epic_events.clients_id_seq OWNED BY epic_events.clients.id;


--
-- TOC entry 222 (class 1259 OID 18262)
-- Name: collaborators; Type: TABLE; Schema: epic_events; Owner: postgres
--

CREATE TABLE epic_events.collaborators (
    id integer NOT NULL,
    name_collaborator character varying,
    contact character varying,
    password_hash character varying,
    department_id integer
);


ALTER TABLE epic_events.collaborators OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 18261)
-- Name: collaborators_id_seq; Type: SEQUENCE; Schema: epic_events; Owner: postgres
--

CREATE SEQUENCE epic_events.collaborators_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE epic_events.collaborators_id_seq OWNER TO postgres;

--
-- TOC entry 4906 (class 0 OID 0)
-- Dependencies: 221
-- Name: collaborators_id_seq; Type: SEQUENCE OWNED BY; Schema: epic_events; Owner: postgres
--

ALTER SEQUENCE epic_events.collaborators_id_seq OWNED BY epic_events.collaborators.id;


--
-- TOC entry 220 (class 1259 OID 18251)
-- Name: companies; Type: TABLE; Schema: epic_events; Owner: postgres
--

CREATE TABLE epic_events.companies (
    id integer NOT NULL,
    name_company character varying
);


ALTER TABLE epic_events.companies OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 18250)
-- Name: companies_id_seq; Type: SEQUENCE; Schema: epic_events; Owner: postgres
--

CREATE SEQUENCE epic_events.companies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE epic_events.companies_id_seq OWNER TO postgres;

--
-- TOC entry 4907 (class 0 OID 0)
-- Dependencies: 219
-- Name: companies_id_seq; Type: SEQUENCE OWNED BY; Schema: epic_events; Owner: postgres
--

ALTER SEQUENCE epic_events.companies_id_seq OWNED BY epic_events.companies.id;


--
-- TOC entry 226 (class 1259 OID 18297)
-- Name: contracts; Type: TABLE; Schema: epic_events; Owner: postgres
--

CREATE TABLE epic_events.contracts (
    id integer NOT NULL,
    client_id integer,
    total_amount double precision,
    remaining_amount double precision,
    creation_date date,
    status boolean
);


ALTER TABLE epic_events.contracts OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 18296)
-- Name: contracts_id_seq; Type: SEQUENCE; Schema: epic_events; Owner: postgres
--

CREATE SEQUENCE epic_events.contracts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE epic_events.contracts_id_seq OWNER TO postgres;

--
-- TOC entry 4908 (class 0 OID 0)
-- Dependencies: 225
-- Name: contracts_id_seq; Type: SEQUENCE OWNED BY; Schema: epic_events; Owner: postgres
--

ALTER SEQUENCE epic_events.contracts_id_seq OWNED BY epic_events.contracts.id;


--
-- TOC entry 218 (class 1259 OID 18240)
-- Name: departments; Type: TABLE; Schema: epic_events; Owner: postgres
--

CREATE TABLE epic_events.departments (
    id integer NOT NULL,
    name_department character varying
);


ALTER TABLE epic_events.departments OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 18239)
-- Name: departments_id_seq; Type: SEQUENCE; Schema: epic_events; Owner: postgres
--

CREATE SEQUENCE epic_events.departments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE epic_events.departments_id_seq OWNER TO postgres;

--
-- TOC entry 4909 (class 0 OID 0)
-- Dependencies: 217
-- Name: departments_id_seq; Type: SEQUENCE OWNED BY; Schema: epic_events; Owner: postgres
--

ALTER SEQUENCE epic_events.departments_id_seq OWNED BY epic_events.departments.id;


--
-- TOC entry 228 (class 1259 OID 18309)
-- Name: events; Type: TABLE; Schema: epic_events; Owner: postgres
--

CREATE TABLE epic_events.events (
    id integer NOT NULL,
    event_name character varying,
    contract_id integer,
    support_id integer,
    location character varying,
    participants integer,
    notes character varying,
    start_date timestamp without time zone,
    end_date timestamp without time zone
);


ALTER TABLE epic_events.events OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 18308)
-- Name: events_id_seq; Type: SEQUENCE; Schema: epic_events; Owner: postgres
--

CREATE SEQUENCE epic_events.events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE epic_events.events_id_seq OWNER TO postgres;

--
-- TOC entry 4910 (class 0 OID 0)
-- Dependencies: 227
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: epic_events; Owner: postgres
--

ALTER SEQUENCE epic_events.events_id_seq OWNED BY epic_events.events.id;


--
-- TOC entry 4718 (class 2604 OID 18281)
-- Name: clients id; Type: DEFAULT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.clients ALTER COLUMN id SET DEFAULT nextval('epic_events.clients_id_seq'::regclass);


--
-- TOC entry 4717 (class 2604 OID 18265)
-- Name: collaborators id; Type: DEFAULT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.collaborators ALTER COLUMN id SET DEFAULT nextval('epic_events.collaborators_id_seq'::regclass);


--
-- TOC entry 4716 (class 2604 OID 18254)
-- Name: companies id; Type: DEFAULT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.companies ALTER COLUMN id SET DEFAULT nextval('epic_events.companies_id_seq'::regclass);


--
-- TOC entry 4719 (class 2604 OID 18300)
-- Name: contracts id; Type: DEFAULT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.contracts ALTER COLUMN id SET DEFAULT nextval('epic_events.contracts_id_seq'::regclass);


--
-- TOC entry 4715 (class 2604 OID 18243)
-- Name: departments id; Type: DEFAULT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.departments ALTER COLUMN id SET DEFAULT nextval('epic_events.departments_id_seq'::regclass);


--
-- TOC entry 4720 (class 2604 OID 18312)
-- Name: events id; Type: DEFAULT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.events ALTER COLUMN id SET DEFAULT nextval('epic_events.events_id_seq'::regclass);


--
-- TOC entry 4895 (class 0 OID 18278)
-- Dependencies: 224
-- Data for Name: clients; Type: TABLE DATA; Schema: epic_events; Owner: postgres
--

COPY epic_events.clients (id, name_client, email, phone, creation_date, update_date, company_id, commercial_id) FROM stdin;
\.


--
-- TOC entry 4893 (class 0 OID 18262)
-- Dependencies: 222
-- Data for Name: collaborators; Type: TABLE DATA; Schema: epic_events; Owner: postgres
--

COPY epic_events.collaborators (id, name_collaborator, contact, password_hash, department_id) FROM stdin;
1	Fouchal Sami	0649716105	$2b$12$kgqamgMdgvMdafUbmCAjiuV2rv.3IGaGlYALCVp2tH8S9beOY5sHG	1
\.


--
-- TOC entry 4891 (class 0 OID 18251)
-- Dependencies: 220
-- Data for Name: companies; Type: TABLE DATA; Schema: epic_events; Owner: postgres
--

COPY epic_events.companies (id, name_company) FROM stdin;
\.


--
-- TOC entry 4897 (class 0 OID 18297)
-- Dependencies: 226
-- Data for Name: contracts; Type: TABLE DATA; Schema: epic_events; Owner: postgres
--

COPY epic_events.contracts (id, client_id, total_amount, remaining_amount, creation_date, status) FROM stdin;
\.


--
-- TOC entry 4889 (class 0 OID 18240)
-- Dependencies: 218
-- Data for Name: departments; Type: TABLE DATA; Schema: epic_events; Owner: postgres
--

COPY epic_events.departments (id, name_department) FROM stdin;
1	gestion
2	commercial
3	support
\.


--
-- TOC entry 4899 (class 0 OID 18309)
-- Dependencies: 228
-- Data for Name: events; Type: TABLE DATA; Schema: epic_events; Owner: postgres
--

COPY epic_events.events (id, event_name, contract_id, support_id, location, participants, notes, start_date, end_date) FROM stdin;
\.


--
-- TOC entry 4911 (class 0 OID 0)
-- Dependencies: 223
-- Name: clients_id_seq; Type: SEQUENCE SET; Schema: epic_events; Owner: postgres
--

SELECT pg_catalog.setval('epic_events.clients_id_seq', 1, false);


--
-- TOC entry 4912 (class 0 OID 0)
-- Dependencies: 221
-- Name: collaborators_id_seq; Type: SEQUENCE SET; Schema: epic_events; Owner: postgres
--

SELECT pg_catalog.setval('epic_events.collaborators_id_seq', 1, true);


--
-- TOC entry 4913 (class 0 OID 0)
-- Dependencies: 219
-- Name: companies_id_seq; Type: SEQUENCE SET; Schema: epic_events; Owner: postgres
--

SELECT pg_catalog.setval('epic_events.companies_id_seq', 1, false);


--
-- TOC entry 4914 (class 0 OID 0)
-- Dependencies: 225
-- Name: contracts_id_seq; Type: SEQUENCE SET; Schema: epic_events; Owner: postgres
--

SELECT pg_catalog.setval('epic_events.contracts_id_seq', 1, false);


--
-- TOC entry 4915 (class 0 OID 0)
-- Dependencies: 217
-- Name: departments_id_seq; Type: SEQUENCE SET; Schema: epic_events; Owner: postgres
--

SELECT pg_catalog.setval('epic_events.departments_id_seq', 3, true);


--
-- TOC entry 4916 (class 0 OID 0)
-- Dependencies: 227
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: epic_events; Owner: postgres
--

SELECT pg_catalog.setval('epic_events.events_id_seq', 1, false);


--
-- TOC entry 4734 (class 2606 OID 18285)
-- Name: clients clients_pkey; Type: CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.clients
    ADD CONSTRAINT clients_pkey PRIMARY KEY (id);


--
-- TOC entry 4730 (class 2606 OID 18271)
-- Name: collaborators collaborators_name_collaborator_key; Type: CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.collaborators
    ADD CONSTRAINT collaborators_name_collaborator_key UNIQUE (name_collaborator);


--
-- TOC entry 4732 (class 2606 OID 18269)
-- Name: collaborators collaborators_pkey; Type: CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.collaborators
    ADD CONSTRAINT collaborators_pkey PRIMARY KEY (id);


--
-- TOC entry 4726 (class 2606 OID 18260)
-- Name: companies companies_name_company_key; Type: CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.companies
    ADD CONSTRAINT companies_name_company_key UNIQUE (name_company);


--
-- TOC entry 4728 (class 2606 OID 18258)
-- Name: companies companies_pkey; Type: CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.companies
    ADD CONSTRAINT companies_pkey PRIMARY KEY (id);


--
-- TOC entry 4736 (class 2606 OID 18302)
-- Name: contracts contracts_pkey; Type: CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.contracts
    ADD CONSTRAINT contracts_pkey PRIMARY KEY (id);


--
-- TOC entry 4722 (class 2606 OID 18249)
-- Name: departments departments_name_department_key; Type: CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.departments
    ADD CONSTRAINT departments_name_department_key UNIQUE (name_department);


--
-- TOC entry 4724 (class 2606 OID 18247)
-- Name: departments departments_pkey; Type: CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.departments
    ADD CONSTRAINT departments_pkey PRIMARY KEY (id);


--
-- TOC entry 4738 (class 2606 OID 18316)
-- Name: events events_pkey; Type: CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- TOC entry 4740 (class 2606 OID 18291)
-- Name: clients clients_commercial_id_fkey; Type: FK CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.clients
    ADD CONSTRAINT clients_commercial_id_fkey FOREIGN KEY (commercial_id) REFERENCES epic_events.collaborators(id);


--
-- TOC entry 4741 (class 2606 OID 18286)
-- Name: clients clients_company_id_fkey; Type: FK CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.clients
    ADD CONSTRAINT clients_company_id_fkey FOREIGN KEY (company_id) REFERENCES epic_events.companies(id);


--
-- TOC entry 4739 (class 2606 OID 18272)
-- Name: collaborators collaborators_department_id_fkey; Type: FK CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.collaborators
    ADD CONSTRAINT collaborators_department_id_fkey FOREIGN KEY (department_id) REFERENCES epic_events.departments(id);


--
-- TOC entry 4742 (class 2606 OID 18303)
-- Name: contracts contracts_client_id_fkey; Type: FK CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.contracts
    ADD CONSTRAINT contracts_client_id_fkey FOREIGN KEY (client_id) REFERENCES epic_events.clients(id);


--
-- TOC entry 4743 (class 2606 OID 18317)
-- Name: events events_contract_id_fkey; Type: FK CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.events
    ADD CONSTRAINT events_contract_id_fkey FOREIGN KEY (contract_id) REFERENCES epic_events.contracts(id);


--
-- TOC entry 4744 (class 2606 OID 18322)
-- Name: events events_support_id_fkey; Type: FK CONSTRAINT; Schema: epic_events; Owner: postgres
--

ALTER TABLE ONLY epic_events.events
    ADD CONSTRAINT events_support_id_fkey FOREIGN KEY (support_id) REFERENCES epic_events.collaborators(id);


-- Completed on 2024-04-02 17:10:52

--
-- PostgreSQL database dump complete
--

