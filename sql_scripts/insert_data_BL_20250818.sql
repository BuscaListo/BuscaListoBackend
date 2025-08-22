-- Insertar Catalogos

-- Insertar categorias
INSERT INTO categorias (nombre,imagenes,creado_por)
values 	('Medicamentos','[]','anthony'),
		('Repuestos','[]','anthony'),
		('Telefonos','[]','anthony'),
		('TV','[]','anthony'),
		('Comida Rapida','[]','anthony'),
		('Zapatos','[]','anthony'),
		('Suplementos','[]','anthony'),
		('Belleza','[]','anthony'),
		('Ropa','[]','anthony')

-- Insertar SubCategorias
--Medicamentos
INSERT INTO subcategorias (id_categoria, nombre, imagenes, creado_por) VALUES
((select id from categorias where nombre='Medicamentos'), 'Analgésicos'          ,'[]','anthony'),
((select id from categorias where nombre='Medicamentos'), 'Antibióticos'         ,'[]', 'anthony'),
((select id from categorias where nombre='Medicamentos'), 'Antigripales'         ,'[]', 'anthony'),
((select id from categorias where nombre='Medicamentos'), 'Vitaminas'            ,'[]', 'anthony'),
((select id from categorias where nombre='Medicamentos'), 'Medicamentos crónicos','[]', 'anthony');

-- Repuestos
INSERT INTO subcategorias (id_categoria, nombre, imagenes, creado_por) VALUES
((SELECT id FROM categorias WHERE nombre='Repuestos'), 'Repuestos automotrices'          , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Repuestos'), 'Repuestos electrónicos'          , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Repuestos'), 'Repuestos de electrodomésticos'  , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Repuestos'), 'Repuestos industriales'          , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Repuestos'), 'Accesorios'                      , '[]', 'anthony');

-- Telefonos
INSERT INTO subcategorias (id_categoria, nombre, imagenes, creado_por) VALUES
((SELECT id FROM categorias WHERE nombre='Telefonos'), 'Smartphones'            , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Telefonos'), 'Teléfonos básicos'      , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Telefonos'), 'Accesorios para móviles', '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Telefonos'), 'Smartwatches'           , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Telefonos'), 'Tablets'                , '[]', 'anthony');

-- TV
INSERT INTO subcategorias (id_categoria, nombre, imagenes, creado_por) VALUES
((SELECT id FROM categorias WHERE nombre='TV'), 'Televisores LED'   , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='TV'), 'Televisores OLED'  , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='TV'), 'Smart TVs'         , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='TV'), 'Accesorios TV'     , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='TV'), 'Sistemas de sonido', '[]', 'anthony');

-- Comida Rapida
INSERT INTO subcategorias (id_categoria, nombre, imagenes, creado_por) VALUES
((SELECT id FROM categorias WHERE nombre='Comida Rapida'), 'Hamburguesas'   , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Comida Rapida'), 'Pizzas'         , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Comida Rapida'), 'Sandwiches'     , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Comida Rapida'), 'Alitas'         , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Comida Rapida'), 'Comida mexicana', '[]', 'anthony');

-- Zapatos
INSERT INTO subcategorias (id_categoria, nombre, imagenes, creado_por) VALUES
((SELECT id FROM categorias WHERE nombre='Zapatos'), 'Zapatos deportivos', '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Zapatos'), 'Zapatos formales'  , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Zapatos'), 'Sandalias'         , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Zapatos'), 'Botas'             , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Zapatos'), 'Tacones'           , '[]', 'anthony');

-- Suplementos
INSERT INTO subcategorias (id_categoria, nombre, imagenes, creado_por) VALUES
((SELECT id FROM categorias WHERE nombre='Suplementos'), 'Proteínas'           , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Suplementos'), 'Creatina'            , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Suplementos'), 'Vitaminas deportivas', '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Suplementos'), 'Quemadores de grasa' , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Suplementos'), 'Aminoácidos'         , '[]', 'anthony');

-- Belleza
INSERT INTO subcategorias (id_categoria, nombre, imagenes, creado_por) VALUES
((SELECT id FROM categorias WHERE nombre='Belleza'), 'Maquillaje'               , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Belleza'), 'Cuidado facial'           , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Belleza'), 'Cuidado corporal'         , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Belleza'), 'Perfumes'                 , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Belleza'), 'Productos para el cabello', '[]', 'anthony');

-- Ropa
INSERT INTO subcategorias (id_categoria, nombre, imagenes, creado_por) VALUES
((SELECT id FROM categorias WHERE nombre='Ropa'), 'Ropa deportiva'    , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Ropa'), 'Ropa casual'       , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Ropa'), 'Ropa formal'       , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Ropa'), 'Ropa interior'     , '[]', 'anthony'),
((SELECT id FROM categorias WHERE nombre='Ropa'), 'Accesorios de moda', '[]', 'anthony');

--Insertar Ubicaciones
INSERT INTO UBICACIONES (nombre, latitud, longitud) VALUES
('Tiendas Daka Valera | Electrodomésticos', '9.3207435','-70.6001511'),
('Daka Agencia Centro Valencia','10.182419388419223','-68.0020493386298'),
('Farmatodo Ccs Carlota','10.500840809426903','-66.83359773062556'),
('Farmatodo Valera, La Plata','9.317902625420613','-70.60319198007946'),
('Farmatodo Valera, Centro','9.302348925654796','-70.61860742459686');

--Insertar Empresas
INSERT INTO empresa (nombre,telefono,id_ubicacion,logo) VALUES
('Farmatodo','+58',3, 'https://www.farmatodo.com.ve/assets/svg/logo-farmatodo-blue.svg'),
('Daka','+58',2,'https://tiendasdaka.com/img/logoF.webp');

-- Insertar Usuarios
INSERT INTO Usuario (nombre, email, password, creado_por) VALUES
('Ernesto Flores','ernestoflores@gmail.com','123','anthony'),
('Samuel Betacourt','samubeta@gmail.com','123','anthony');

--Insertar Sucursales
INSERT INTO Sucursales (nombre, imagenes, id_empresa, id_ubicacion, id_usuario) VALUES
('Tiendas Daka Valera','["https://lh3.googleusercontent.com/p/AF1QipMCJ1SeWEtTumTSrVu6b5hY-TkLMdQmW2wzc8hP=s1360-w1360-h1020-rw","https://lh3.googleusercontent.com/p/AF1QipPpAhNwN0MOP_2ChyzTbGAx9G52RLXfaehSioCq=s1360-w1360-h1020-rw"]'
,2,1,1
),
('Farmatodo Centro de Valera', '[]'
,1,5,2
);

--Insertar Catalogo de permisos
INSERT INTO catalogo_permisos (nombre, creado_por) VALUES
('view_products_basic','anthony'),
('view_products_medium','anthony'),
('view_products_premium','anthony'),
('view_advertisements_basic','anthony'),
('view_advertisements_medium','anthony'),
('view_advertisements_premium','anthony'),
('priority_list_basic','anthony'),
('priority_list_medium','anthony'),
('priority_list_premium','anthony'),
('location_basic','anthony'),
('location_medium','anthony'),
('location_premium','anthony'),
('statistics_basic','anthony'),
('statistics_medium','anthony'),
('statistics_premium','anthony'),
('support_basic','anthony'),
('support_medium','anthony'),
('support_premium','anthony'),
('extra_basic','anthony'),
('extra_medium','anthony'),
('extra_premium','anthony');

-- Insertar permisos de usuario
INSERT INTO permisos_usuarios (id_usuario,id_catalogo_permiso,read,write,delete,edit,creado_por)
SELECT  1 id_usuario, id id_catalogo_permiso,True read,True write,True delete,True edit,'anthony' creado_por
FROM catalogo_permisos
where nombre like '%basic%'

INSERT INTO permisos_usuarios (id_usuario,id_catalogo_permiso,read,write,delete,edit,creado_por)
SELECT  2 id_usuario, id id_catalogo_permiso,True read,True write,True delete,True edit,'anthony' creado_por
FROM catalogo_permisos
where nombre like '%premium%'

--Insertar Marca
INSERT INTO marcas (nombre, descripcion, imagenes, logo, creado_por) VALUES
('Laboratorios Farma', 'Laboratorios Farma', '[]','','anthony'),
('Calox', 'Calox', '[]','','anthony'),
('La Sante', 'La Sante', '[]','','anthony'),
('Siragon', 'Siragon', '[]','','anthony'),
('Bremen', 'Bremen', '[]','','anthony');

-- Insertar Productos
INSERT INTO Producto (nombre, descripcion, imagenes, precio_bs,precio_dls,in_stock,id_sub_categoria,id_sucursal,
id_marca,creado_por,caracteristicas,caracteristicas_avanzada) VALUES
('Cetirizina 10 mg','Cetirizina 10 mg Cetral Siegfried Caja x 10 Tabletas',
'["https://lh3.googleusercontent.com/6WcSk-vyHvlYq2iWh0Rmxpz65QnJMo2QYnb4xLs9s_6qcjPmfO0swWFxcTKWtqR6lfhOeHBTsuYMRyyZVgP4kvznfaFtu9R_JHIUd6J-TJ7voiuw",
"https://lh3.googleusercontent.com/QMDo6lSz4CHTBXHLuHGpM-2lc1E2S5jwHDLJfJq4GkVBYynsB4MUnsCQ_Qtb39D8luX0WuGoQAN4iGB3x_GSg1tqHRkfVTWTMeRxeHG-OXb46YA",
"https://lh3.googleusercontent.com/unGGeNxCAafZp-N84PQveoh3lrnHYYpVFQwmk8fwZ66liEBNr2Pxh2vQQiQGdDVGEopsM9hvrVw_l9oe1W8sqTziCBQeY_TsC0p-8AR5nedhkDwicA"]'
,'223.85','1.6',1,3,2,1,'anthony','["reacciones":"somnolencia, fatiga. Además, en ads.: cefalea, mareo, sequedad de boca, dolor abdominal, faringitis, náuseas y en niños 6 meses-12 años: diarrea, rinitis.","lactancia":"evitar"]',
'[]'
)

INSERT INTO Producto (nombre, descripcion, imagenes, precio_bs,precio_dls,in_stock,id_sub_categoria,id_sucursal,
id_marca,creado_por,caracteristicas,caracteristicas_avanzada) VALUES
('Vitamina D','Vitamina D Farma D 2000Ui Laboratorios Farma Caja x 30 Tabletas',
'["https://lh3.googleusercontent.com/jQkeFMDQ9X5eTcvBrWCs4w68cRD9U6PajjXswWBYp7PBTcyxvobvhynzL8mhao30c81cR1yUw6Jt3bpjJDsKiW-FpDRZ9lR8XG8",
"https://lh3.googleusercontent.com/ul6sDg8l8FQMHXEXiKZgr5wNT8XZkWAyIetre9cyyF8jXsPGyneu_xVuuVuv3COlwguL39I0xbQErIral9s7YOe-sVv3z20wzpKwxjqUUbRBqO8z"
]'
,'759.94',null,1,4,2,1,'anthony','["reacciones":"somnolencia, fatiga. Además, en ads.: cefalea, mareo, sequedad de boca, dolor abdominal, faringitis, náuseas y en niños 6 meses-12 años: diarrea, rinitis.","lactancia":"evitar"]',
'[]'
)

--INSERTAR SUBSCRIPCIONES
INSERT INTO subscripciones (nombre, precio, anuncios, prioridad_listado,ubicaciones,estadisticas,soporte, extras,creado_por)
VALUES ('Basico',0,'N','N','Limitadas','N','Basico (FQA/Email)','N','anthony'),
('Medio',10,'S','Med','Sidebar/Secciones Internas','N','Estandar (48h)','Links Personalizados','anthony'),
('Premium',30,'S','Alta','Home+Sidebar+Exclusivas','S','Prioritario (24/7)','Exclusividad en ubicaciones y Campañas Especiales','anthony');

--INSERTAR SUBSCRIPCIONES USUARIO

INSERT INTO subcripcion_usuario (id_subscripcion,id_usuario,creado_por) VALUES
(1,1,'anthony'),
(3,2,'anthony');

--Reset index table (Tools)
--SELECT setval(pg_get_serial_sequence('categorias', 'id'), 1, false);
