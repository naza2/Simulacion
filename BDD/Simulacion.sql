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
    ubicacion character varying(50) NOT NULL,
    tiempo_promedio_atencion numeric,
    flujo_clientes integer,
    variedad_productos integer,
    calidad_comida integer,
    precios integer,
    CONSTRAINT casetas_calidad_comida_check CHECK (((calidad_comida >= 1) AND (calidad_comida <= 5))),
    CONSTRAINT casetas_precios_check CHECK (((precios >= 1) AND (precios <= 5))),
    CONSTRAINT casetas_variedad_productos_check CHECK (((variedad_productos >= 1) AND (variedad_productos <= 5)))
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
    semestre character varying(40),
    frecuencia_compra character varying(40),
    horario_preferido character varying(40),
    horas_libres character varying(40),
    caseta_preferida character varying(50),
    factor_influencia character varying(40),
    tiempo_espera_dispuesto character varying(40),
    presupuesto character varying(40),
    experiencia_general integer,
    experiencia_filas character varying(5),
    espera_promedio_filas character varying(40),
    id_caseta integer
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
    id_observacion integer,
    hora_intervalo time without time zone,
    personas_en_fila integer
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
-- Name: observaciones_caseta; Type: TABLE; Schema: public; Owner: diego
--

CREATE TABLE public.observaciones_caseta (
    id_observacion integer NOT NULL,
    caseta character varying(50),
    fecha date,
    hora_inicio time without time zone,
    hora_fin time without time zone,
    clientes_totales integer,
    tiempo_promedio_atencion double precision
);


ALTER TABLE public.observaciones_caseta OWNER TO diego;

--
-- Name: observaciones_caseta_id_observacion_seq; Type: SEQUENCE; Schema: public; Owner: diego
--

CREATE SEQUENCE public.observaciones_caseta_id_observacion_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.observaciones_caseta_id_observacion_seq OWNER TO diego;

--
-- Name: observaciones_caseta_id_observacion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: diego
--

ALTER SEQUENCE public.observaciones_caseta_id_observacion_seq OWNED BY public.observaciones_caseta.id_observacion;


--
-- Name: tiempos_atencion; Type: TABLE; Schema: public; Owner: diego
--

CREATE TABLE public.tiempos_atencion (
    id_tiempo integer NOT NULL,
    id_observacion integer,
    tiempo_atencion double precision
);


ALTER TABLE public.tiempos_atencion OWNER TO diego;

--
-- Name: tiempos_atencion_id_tiempo_seq; Type: SEQUENCE; Schema: public; Owner: diego
--

CREATE SEQUENCE public.tiempos_atencion_id_tiempo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tiempos_atencion_id_tiempo_seq OWNER TO diego;

--
-- Name: tiempos_atencion_id_tiempo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: diego
--

ALTER SEQUENCE public.tiempos_atencion_id_tiempo_seq OWNED BY public.tiempos_atencion.id_tiempo;


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
-- Name: observaciones_caseta id_observacion; Type: DEFAULT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.observaciones_caseta ALTER COLUMN id_observacion SET DEFAULT nextval('public.observaciones_caseta_id_observacion_seq'::regclass);


--
-- Name: tiempos_atencion id_tiempo; Type: DEFAULT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.tiempos_atencion ALTER COLUMN id_tiempo SET DEFAULT nextval('public.tiempos_atencion_id_tiempo_seq'::regclass);


--
-- Data for Name: casetas; Type: TABLE DATA; Schema: public; Owner: diego
--

COPY public.casetas (id_caseta, nombre_caseta, ubicacion, tiempo_promedio_atencion, flujo_clientes, variedad_productos, calidad_comida, precios) FROM stdin;
3	Lado Chedraui	Aun lado de chedraui	4	4	4	4	4
2	Caseta Blanca	Aun lado del centro de informacion	1	2	3	3	3
1	CafeITO	Atras del centro de informacion	2	2	3	2	2
\.


--
-- Data for Name: encuestas_estudiantes; Type: TABLE DATA; Schema: public; Owner: diego
--

COPY public.encuestas_estudiantes (id_encuesta, semestre, frecuencia_compra, horario_preferido, horas_libres, caseta_preferida, factor_influencia, tiempo_espera_dispuesto, presupuesto, experiencia_general, experiencia_filas, espera_promedio_filas, id_caseta) FROM stdin;
1	Primero	Diariamente	10-12	2 horas	CafeITO	Calidad	menos de 5	30 - 50	5	Sí	10 - 20 min	\N
2	Tercero	2 - 3 veces	12-2	1 hora	Caseta Blanca	Precios	5 - 10 min	50 - 70	4	Sí	20 - 30 min	\N
3	Quinto	1 vez	8-10	3 horas	CafeITO	Atención	menos de 5	30 - 50	3	No	\N	\N
4	Septimo	Diariamente	10-12	1 hora	Lado Chedraui	Variedad	menos de 5	50 - 70	4	Sí	10 - 20 min	\N
5	Noveno	Nunca	no tengo horario especifico	No tengo libre	Caseta Blanca	Rapidez	5 - 10 min	menos de 30	2	No	\N	\N
6	Primero	2 - 3 veces	10-12	2 horas	CafeITO	Calidad	10 - 15 min	30 - 50	3	Sí	10 - 20 min	\N
7	Tercero	Diaramente	8-10	3 horas	Lado Chedraui	Espacio	5 - 10 min	50 - 70	4	Sí	10 - 20 min	\N
8	Quinto	1 vez	2-4	2 horas	Caseta Blanca	Precios	15 - 20 min	50 - 70	3	No	\N	\N
\.


--
-- Data for Name: intervalos_fila; Type: TABLE DATA; Schema: public; Owner: diego
--

COPY public.intervalos_fila (id_intervalo, id_observacion, hora_intervalo, personas_en_fila) FROM stdin;
1	1	11:25:00	3
2	1	11:30:00	1
3	1	11:35:00	2
4	1	11:40:00	2
5	1	11:45:00	5
6	1	11:50:00	4
7	1	11:55:00	1
8	1	12:00:00	5
9	1	12:05:00	8
10	1	12:10:00	3
11	2	16:25:00	4
12	2	16:30:00	3
13	2	16:35:00	2
14	2	16:40:00	5
15	2	16:45:00	6
16	2	16:50:00	3
17	2	16:55:00	1
18	2	17:00:00	8
19	2	17:05:00	2
20	2	17:10:00	5
21	3	10:05:00	8
22	3	10:10:00	14
23	3	10:15:00	11
24	3	10:20:00	7
25	3	10:25:00	10
26	3	10:30:00	11
27	3	10:35:00	12
28	3	10:40:00	8
29	3	10:45:00	14
30	3	10:50:00	13
31	4	10:05:00	8
32	4	10:10:00	7
33	4	10:15:00	7
34	4	10:20:00	6
35	4	10:25:00	3
36	4	10:30:00	1
37	4	10:35:00	6
38	4	10:40:00	2
39	4	10:45:00	4
40	4	10:50:00	5
41	5	10:10:00	13
42	5	10:15:00	9
43	5	10:20:00	9
44	5	10:25:00	5
45	5	10:30:00	11
46	5	10:35:00	7
47	5	10:40:00	2
48	5	10:45:00	2
49	5	10:50:00	5
50	5	10:55:00	9
\.


--
-- Data for Name: observaciones_caseta; Type: TABLE DATA; Schema: public; Owner: diego
--

COPY public.observaciones_caseta (id_observacion, caseta, fecha, hora_inicio, hora_fin, clientes_totales, tiempo_promedio_atencion) FROM stdin;
1	Caseta Blanca	2023-10-25	11:20:00	12:20:00	40	2.31
2	CafeITO	2023-10-25	16:20:00	17:20:00	43	3.59
3	Caseta Blanca	2023-10-28	10:00:00	11:00:00	143	1.41
4	CafeITO	2023-10-29	10:00:00	11:00:00	27	4.05
5	Caseta Blanca	2023-10-29	10:00:00	11:00:00	89	4.4
6	CafeITO	2023-10-29	16:00:00	17:00:00	39	3.86
7	Caseta Blanca	2023-10-30	12:00:00	13:00:00	35	2.83
8	CafeITO	2023-10-30	12:00:00	13:00:00	22	3.19
9	Caseta Blanca	2023-10-31	10:00:00	11:00:00	50	3.05
10	CafeITO	2023-10-31	14:00:00	15:00:00	60	2.95
11	Caseta Blanca	2023-10-25	11:20:00	12:20:00	40	2.31
12	CafeITO	2023-10-25	16:20:00	17:20:00	43	3.59
13	Caseta Blanca	2023-10-28	10:00:00	11:00:00	143	1.41
14	CafeITO	2023-10-29	10:00:00	11:00:00	27	4.05
15	Caseta Blanca	2023-10-29	10:00:00	11:00:00	89	4.4
16	CafeITO	2023-10-29	16:00:00	17:00:00	39	3.86
17	Caseta Blanca	2023-10-30	12:00:00	13:00:00	35	2.83
18	CafeITO	2023-10-30	12:00:00	13:00:00	22	3.19
19	Caseta Blanca	2023-10-31	10:00:00	11:00:00	50	3.05
20	CafeITO	2023-10-31	14:00:00	15:00:00	60	2.95
\.


--
-- Data for Name: tiempos_atencion; Type: TABLE DATA; Schema: public; Owner: diego
--

COPY public.tiempos_atencion (id_tiempo, id_observacion, tiempo_atencion) FROM stdin;
1	1	2.13
2	1	3.3
3	1	3.2
4	1	0.56
5	1	1.1
6	1	1.27
7	1	3.33
8	1	1.4
9	1	6.2
10	1	1.1
11	2	1.4
12	2	1.2
13	2	1.8
14	2	5.1
15	2	5.6
16	2	2.3
17	2	5.4
18	2	3.2
19	2	5.7
20	2	2.9
21	3	0.34
22	3	1.12
23	3	2.45
24	3	0.08
25	3	3.27
26	3	4.53
27	3	0.19
28	3	1.41
29	3	0.06
30	3	2.29
31	4	1.06
32	4	4.46
33	4	1.5
34	4	3.5
35	4	4.2
36	4	1.29
37	4	3.46
38	4	4.32
39	4	4.45
40	4	5.29
41	5	0.45
42	5	1.12
43	5	2.05
44	5	3.27
45	5	4.38
46	5	5.5
47	5	6.15
48	5	7.22
49	5	8.34
50	5	9.01
51	6	2
52	6	5.2
53	6	5.7
54	6	5.6
55	6	5.6
56	6	2.8
57	6	1.4
58	6	5.4
59	6	5.3
60	6	5
61	7	0.37
62	7	2.03
63	7	3.41
64	7	2.01
65	7	0.36
66	7	2.25
67	7	1.4
68	7	3.43
69	7	4.2
70	7	6.4
71	8	0.37
72	8	2.03
73	8	3.41
74	8	2.01
75	8	0.36
76	8	2.25
77	8	1.4
78	8	3.43
79	8	4.2
80	8	6.4
81	9	2.12
82	9	3.25
83	9	1.95
84	9	4.37
85	9	2.9
86	9	2.83
87	9	2.45
88	9	3.18
89	9	3.02
90	9	1.78
91	10	3.25
92	10	4.1
93	10	3.45
94	10	2.9
95	10	3.85
96	10	4.2
97	10	3.15
98	10	4.05
99	10	3.9
100	10	4.3
\.


--
-- Name: casetas_id_caseta_seq; Type: SEQUENCE SET; Schema: public; Owner: diego
--

SELECT pg_catalog.setval('public.casetas_id_caseta_seq', 1, false);


--
-- Name: encuestas_estudiantes_id_encuesta_seq; Type: SEQUENCE SET; Schema: public; Owner: diego
--

SELECT pg_catalog.setval('public.encuestas_estudiantes_id_encuesta_seq', 8, true);


--
-- Name: intervalos_fila_id_intervalo_seq; Type: SEQUENCE SET; Schema: public; Owner: diego
--

SELECT pg_catalog.setval('public.intervalos_fila_id_intervalo_seq', 50, true);


--
-- Name: observaciones_caseta_id_observacion_seq; Type: SEQUENCE SET; Schema: public; Owner: diego
--

SELECT pg_catalog.setval('public.observaciones_caseta_id_observacion_seq', 20, true);


--
-- Name: tiempos_atencion_id_tiempo_seq; Type: SEQUENCE SET; Schema: public; Owner: diego
--

SELECT pg_catalog.setval('public.tiempos_atencion_id_tiempo_seq', 100, true);


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
-- Name: observaciones_caseta observaciones_caseta_pkey; Type: CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.observaciones_caseta
    ADD CONSTRAINT observaciones_caseta_pkey PRIMARY KEY (id_observacion);


--
-- Name: tiempos_atencion tiempos_atencion_pkey; Type: CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.tiempos_atencion
    ADD CONSTRAINT tiempos_atencion_pkey PRIMARY KEY (id_tiempo);


--
-- Name: encuestas_estudiantes encuestas_estudiantes_id_caseta_fkey; Type: FK CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.encuestas_estudiantes
    ADD CONSTRAINT encuestas_estudiantes_id_caseta_fkey FOREIGN KEY (id_caseta) REFERENCES public.casetas(id_caseta);


--
-- Name: intervalos_fila intervalos_fila_id_observacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.intervalos_fila
    ADD CONSTRAINT intervalos_fila_id_observacion_fkey FOREIGN KEY (id_observacion) REFERENCES public.observaciones_caseta(id_observacion);


--
-- Name: tiempos_atencion tiempos_atencion_id_observacion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: diego
--

ALTER TABLE ONLY public.tiempos_atencion
    ADD CONSTRAINT tiempos_atencion_id_observacion_fkey FOREIGN KEY (id_observacion) REFERENCES public.observaciones_caseta(id_observacion);


--
-- PostgreSQL database dump complete
--

