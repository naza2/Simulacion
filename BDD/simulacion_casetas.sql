--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: casetas; Type: TABLE; Schema: public; Owner: diego
--

CREATE TABLE public.casetas (
    id_caseta integer NOT NULL,
    nombre_caseta character varying(50) NOT NULL,
    ubicacion character varying(100)
);


ALTER TABLE public.casetas OWNER TO diego;

--
-- Name: casetas_id_caseta_seq; Type: SEQUENCE; Schema: public; Owner: diego
--

CREATE SEQUENCE public.casetas_id_caseta_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.casetas_id_caseta_seq OWNER TO diego;

--
-- Name: casetas_id_caseta_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: diego
--

ALTER SEQUENCE public.casetas_id_caseta_seq OWNED BY public.casetas.id_caseta;


--
-- Name: encuestas_estudiantes; Type: TABLE; Schema: public; Owner: diego
--

CREATE TABLE public.encuestas_estudiantes (
    id_encuesta integer NOT NULL,
    semestre character varying(20) NOT NULL,
    frecuencia_compra character varying(20) NOT NULL,
    horario_preferido character varying(20),
    horas_libres character varying(20),
    caseta_preferida integer,
    factores_influencia character varying(100),
    tiempo_dispuesto_esperar character varying(20),
    presupuesto character varying(20),
    experiencia_calificacion integer,
    experiencia_fila boolean,
    tiempo_espera_promedio character varying(20),
    CONSTRAINT encuestas_estudiantes_experiencia_calificacion_check CHECK (((experiencia_calificacion >= 1) AND (experiencia_calificacion <= 5)))
);


ALTER TABLE public.encuestas_estudiantes OWNER TO diego;

--
-- Name: encuestas_estudiantes_id_encuesta_seq; Type: SEQUENCE; Schema: public; Owner: diego
--

CREATE SEQUENCE public.encuestas_estudiantes_id_encuesta_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.encuestas_estudiantes_id_encuesta_seq OWNER TO diego;

--
-- Name: encuestas_estudiantes_id_encuesta_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: diego
--

ALTER SEQUENCE public.encuestas_estudiantes_id_encuesta_seq OWNED BY public.encuestas_estudiantes.id_encuesta;


--
-- Name: intervalos_fila; Type: TABLE; Schema: public; Owner: diego
--

CREATE TABLE public.intervalos_fila (
    id_intervalo integer NOT NULL,
    hora_observacion time without time zone NOT NULL,
    personas_en_fila integer NOT NULL,
    id_observacion integer
);


ALTER TABLE public.intervalos_fila OWNER TO diego;

--
-- Name: intervalos_fila_id_intervalo_seq; Type: SEQUENCE; Schema: public; Owner: diego
--

CREATE SEQUENCE public.intervalos_fila_id_intervalo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.intervalos_fila_id_intervalo_seq OWNER TO diego;

--
-- Name: intervalos_fila_id_intervalo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: diego
--

ALTER SEQUENCE public.intervalos_fila_id_intervalo_seq OWNED BY public.intervalos_fila.id_intervalo;


--
-- Name: observaciones_por_hora; Type: TABLE; Schema: public; Owner: diego
--

CREATE TABLE public.observaciones_por_hora (
    id_observacion integer NOT NULL,
    fecha date NOT NULL,
    hora_inicio time without time zone NOT NULL,
    hora_fin time without time zone NOT NULL,
    total_clientes integer NOT NULL,
    promedio_tiempo double precision NOT NULL,
    id_caseta integer
);


ALTER TABLE public.observaciones_por_hora OWNER TO diego;

--
-- Name: observaciones_por_hora_id_observacion_seq; Type: SEQUENCE; Schema: public; Owner: diego
--

CREATE SEQUENCE public.observaciones_por_hora_id_observacion_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.observaciones_por_hora_id_observacion_seq OWNER TO diego;

--
-- Name: observaciones_por_hora_id_observacion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: diego
--

ALTER SEQUENCE public.observaciones_por_hora_id_observacion_seq OWNED BY public.observaciones_por_hora.id_observacion;


--
-- Name: casetas id_caseta; Type: DEFAULT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.casetas ALTER COLUMN id_caseta SET DEFAULT nextval('public.casetas_id_caseta_seq'::regclass);


--
-- Name: encuestas_estudiantes id_encuesta; Type: DEFAULT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.encuestas_estudiantes ALTER COLUMN id_encuesta SET DEFAULT nextval('public.encuestas_estudiantes_id_encuesta_seq'::regclass);


--
-- Name: intervalos_fila id_intervalo; Type: DEFAULT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.intervalos_fila ALTER COLUMN id_intervalo SET DEFAULT nextval('public.intervalos_fila_id_intervalo_seq'::regclass);


--
-- Name: observaciones_por_hora id_observacion; Type: DEFAULT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.observaciones_por_hora ALTER COLUMN id_observacion SET DEFAULT nextval('public.observaciones_por_hora_id_observacion_seq'::regclass);


--
-- Data for Name: casetas; Type: TABLE DATA; Schema: public; Owner: diego
--

COPY public.casetas (id_caseta, nombre_caseta, ubicacion) FROM stdin;
\.


--
-- Data for Name: encuestas_estudiantes; Type: TABLE DATA; Schema: public; Owner: diego
--

COPY public.encuestas_estudiantes (id_encuesta, semestre, frecuencia_compra, horario_preferido, horas_libres, caseta_preferida, factores_influencia, tiempo_dispuesto_esperar, presupuesto, experiencia_calificacion, experiencia_fila, tiempo_espera_promedio) FROM stdin;
\.


--
-- Data for Name: intervalos_fila; Type: TABLE DATA; Schema: public; Owner: diego
--

COPY public.intervalos_fila (id_intervalo, hora_observacion, personas_en_fila, id_observacion) FROM stdin;
\.


--
-- Data for Name: observaciones_por_hora; Type: TABLE DATA; Schema: public; Owner: diego
--

COPY public.observaciones_por_hora (id_observacion, fecha, hora_inicio, hora_fin, total_clientes, promedio_tiempo, id_caseta) FROM stdin;
\.


--
-- Name: casetas_id_caseta_seq; Type: SEQUENCE SET; Schema: public; Owner: diego
--

SELECT pg_catalog.setval('public.casetas_id_caseta_seq', 1, false);


--
-- Name: encuestas_estudiantes_id_encuesta_seq; Type: SEQUENCE SET; Schema: public; Owner: diego
--

SELECT pg_catalog.setval('public.encuestas_estudiantes_id_encuesta_seq', 1, false);


--
-- Name: intervalos_fila_id_intervalo_seq; Type: SEQUENCE SET; Schema: public; Owner: diego
--

SELECT pg_catalog.setval('public.intervalos_fila_id_intervalo_seq', 1, false);


--
-- Name: observaciones_por_hora_id_observacion_seq; Type: SEQUENCE SET; Schema: public; Owner: diego
--

SELECT pg_catalog.setval('public.observaciones_por_hora_id_observacion_seq', 1, false);


--
-- Name: casetas casetas_pkey; Type: CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.casetas
    ADD CONSTRAINT casetas_pkey PRIMARY KEY (id_caseta);


--
-- Name: encuestas_estudiantes encuestas_estudiantes_pkey; Type: CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.encuestas_estudiantes
    ADD CONSTRAINT encuestas_estudiantes_pkey PRIMARY KEY (id_encuesta);


--
-- Name: intervalos_fila intervalos_fila_pkey; Type: CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.intervalos_fila
    ADD CONSTRAINT intervalos_fila_pkey PRIMARY KEY (id_intervalo);


--
-- Name: observaciones_por_hora observaciones_por_hora_pkey; Type: CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.observaciones_por_hora
    ADD CONSTRAINT observaciones_por_hora_pkey PRIMARY KEY (id_observacion);


--
-- Name: encuestas_estudiantes encuestas_estudiantes_caseta_preferida_fkey; Type: FK CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.encuestas_estudiantes
    ADD CONSTRAINT encuestas_estudiantes_caseta_preferida_fkey FOREIGN KEY (caseta_preferida) REFERENCES public.casetas(id_caseta);


--
-- Name: intervalos_fila intervalos_fila_id_observacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.intervalos_fila
    ADD CONSTRAINT intervalos_fila_id_observacion_fkey FOREIGN KEY (id_observacion) REFERENCES public.observaciones_por_hora(id_observacion);


--
-- Name: observaciones_por_hora observaciones_por_hora_id_caseta_fkey; Type: FK CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.observaciones_por_hora
    ADD CONSTRAINT observaciones_por_hora_id_caseta_fkey FOREIGN KEY (id_caseta) REFERENCES public.casetas(id_caseta);


--
-- PostgreSQL database dump complete
--

