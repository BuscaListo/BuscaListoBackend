CREATE TABLE Producto (
  "id" BIGSERIAL PRIMARY KEY,
  "nombre" VARCHAR NOT NULL,
  "descripcion" TEXT,
  "precio_bs" DOUBLE PRECISION NOT NULL,
  "precio_dls" DOUBLE PRECISION,
  "imagenes" TEXT,
  "codigo" VARCHAR(150),
  "in_stock" SMALLINT NOT NULL DEFAULT 1 CHECK ("in_stock" IN (0, 1)),
  "id_sub_categoria" BIGINT NOT NULL,
  "id_sucursal" BIGINT NOT NULL,
  "id_marca" BIGINT NOT NULL,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(250),
  "activo" SMALLINT NOT NULL DEFAULT 1 CHECK ("activo" IN (0, 1))
);

CREATE TABLE Categorias (
  "id" BIGSERIAL PRIMARY KEY,
  "nombre" VARCHAR NOT NULL,
  "imagenes" TEXT,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE SubCategorias (
  "id" BIGSERIAL PRIMARY KEY,
  "nombre" VARCHAR NOT NULL,
  "imagenes" TEXT,
  "id_categoria" BIGINT NOT NULL,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE Stock (
  "id" BIGSERIAL PRIMARY KEY,
  "id_producto" BIGINT NOT NULL,
  "cantidad_total" INTEGER,
  "cantidad_vendida" INTEGER,
  "cantidad_ofertada" INTEGER,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE Marcas (
  "id" BIGSERIAL PRIMARY KEY,
  "nombre" VARCHAR NOT NULL,
  "descripcion" TEXT,
  "imagenes" TEXT,
  "logo" TEXT,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE Ofertas (
  "id" BIGSERIAL PRIMARY KEY,
  "descripcion" TEXT NOT NULL,
  "porcentaje" DECIMAL(5,2),
  "id_producto" BIGINT,
  "id_categoria" BIGINT,
  "id_sub_categoria" BIGINT,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE Sucursales (
  "id" BIGSERIAL PRIMARY KEY,
  "nombre" VARCHAR NOT NULL,
  "imagenes" TEXT,
  "id_empresa" BIGINT NOT NULL,
  "id_ubicacion" BIGINT NOT NULL,
  "id_usuario" BIGINT NOT NULL,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE Empresa (
  "id" BIGSERIAL PRIMARY KEY,
  "nombre" VARCHAR NOT NULL,
  "telefono" VARCHAR(20),
  "id_ubicacion" BIGINT NOT NULL,
  "logo" TEXT,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE Ubicaciones (
  "id" BIGSERIAL PRIMARY KEY,
  "nombre" VARCHAR NOT NULL,
  "latitud" DECIMAL(10,8) NOT NULL,
  "longitud" DECIMAL(10,8) NOT NULL,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE WEBSERVICE_LOG (
  "id" BIGSERIAL PRIMARY KEY,
  "id_web_service" BIGINT NOT NULL,
  "input" TEXT,
  "error" TEXT,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255)
);

CREATE TABLE WEB_SERVICE (
  "id" BIGSERIAL PRIMARY KEY,
  "nombre" VARCHAR(100),
  "descripcion" VARCHAR(255),
  "url" VARCHAR(255),
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN DEFAULT TRUE
);

CREATE TABLE BITACORA_PRECIO_PRODUCTO (
  "id" BIGSERIAL PRIMARY KEY,
  "id_producto" BIGINT NOT NULL,
  "precio_actualizado" DECIMAL(10,2),
  "precio_nuevo" DECIMAL(10,2),
  "porcentaje" DECIMAL(5,2),
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255)
);

CREATE TABLE CATALOGO_PERMISOS (
  "id" BIGSERIAL PRIMARY KEY,
  "nombre" VARCHAR(100),
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN DEFAULT TRUE
);

CREATE TABLE PERMISOS_USUARIOS (
  "id" BIGSERIAL PRIMARY KEY,
  "id_usuario" BIGINT,
  "id_catalogo_permiso" BIGINT,
  "read" BOOLEAN DEFAULT FALSE,
  "write" BOOLEAN DEFAULT FALSE,
  "delete" BOOLEAN DEFAULT FALSE,
  "edit" BOOLEAN DEFAULT FALSE,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN DEFAULT TRUE
);

CREATE TABLE SUBSCRIPCIONES (
  "id" BIGSERIAL PRIMARY KEY,
  "nombre" VARCHAR(100),
  "precio" DECIMAL(10,2),
  "anuncios" BOOLEAN DEFAULT FALSE,
  "prioridad_listado" BOOLEAN DEFAULT FALSE,
  "ubicaciones" BOOLEAN DEFAULT FALSE,
  "estadisticas" BOOLEAN DEFAULT FALSE,
  "soporte" BOOLEAN DEFAULT FALSE,
  "extras" BOOLEAN DEFAULT FALSE,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN DEFAULT TRUE
);

ALTER TABLE subscripciones 
ALTER COLUMN anuncios TYPE VARCHAR(150),
ALTER COLUMN anuncios SET DEFAULT 'N';

ALTER TABLE subscripciones 
ALTER COLUMN prioridad_listado TYPE VARCHAR(150),
ALTER COLUMN prioridad_listado SET DEFAULT 'N';

ALTER TABLE subscripciones 
ALTER COLUMN ubicaciones TYPE VARCHAR(150),
ALTER COLUMN ubicaciones SET DEFAULT 'N';

ALTER TABLE subscripciones 
ALTER COLUMN estadisticas TYPE VARCHAR(150),
ALTER COLUMN estadisticas SET DEFAULT 'N';

ALTER TABLE subscripciones 
ALTER COLUMN soporte TYPE VARCHAR(150),
ALTER COLUMN soporte SET DEFAULT 'N';

ALTER TABLE subscripciones 
ALTER COLUMN extras TYPE VARCHAR(150),
ALTER COLUMN extras SET DEFAULT 'N';

CREATE TABLE SUBCRIPCION_USUARIO (
  "id" BIGSERIAL PRIMARY KEY,
  "id_subscripcion" BIGINT NOT NULL,
  "id_usuario" BIGINT NOT NULL,
  "activo" BOOLEAN DEFAULT TRUE,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE USUARIO (
  "id" BIGSERIAL PRIMARY KEY,
  "nombre" VARCHAR(100),
  "email" VARCHAR(255) UNIQUE,
  "password" VARCHAR(255),
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN DEFAULT TRUE
);

CREATE TABLE PUBLICIDADES (
  "id" BIGSERIAL PRIMARY KEY,
  "id_sucursal" BIGINT NOT NULL,
  "imagenes_publicidad" TEXT,
  "link_destino" VARCHAR(300),
  "prioridad" INTEGER,
  "fecha_inicio" DATE,
  "fecha_fin" DATE,
  "activo" BOOLEAN DEFAULT TRUE,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ESTADISTICAS_PUBLICIDAD (
  "id" BIGSERIAL PRIMARY KEY,
  "id_publicidad" BIGINT,
  "impresiones" INTEGER,
  "clics" INTEGER,
  "fecha" DATE,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN DEFAULT TRUE
);

CREATE TABLE MONEDA (
  "id" BIGSERIAL PRIMARY KEY,
  "divisa" VARCHAR(150),
  "precio_bs" DECIMAL(10,2),
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN DEFAULT TRUE
);

CREATE TABLE IMAGENES (
  "id" BIGSERIAL PRIMARY KEY,
  "url" VARCHAR(150),
  "id_producto" BIGINT,
  "creado" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  "creado_por" VARCHAR(255),
  "activo" BOOLEAN DEFAULT TRUE
);

ALTER TABLE IMAGENES ADD CONSTRAINT "fk_imagenes_producto" 
FOREIGN KEY ("id_producto") REFERENCES Producto ("id");

ALTER TABLE Producto ADD CONSTRAINT "fk_producto_subcategoria" 
FOREIGN KEY ("id_sub_categoria") REFERENCES SubCategorias ("id");

-- Relación entre Producto y Sucursales (CORRECCIÓN IMPORTANTE)
ALTER TABLE Producto ADD CONSTRAINT "fk_producto_sucursal" 
FOREIGN KEY ("id_sucursal") REFERENCES Sucursales ("id");

-- Relación entre Producto y Marcas (correcta)
ALTER TABLE Producto ADD CONSTRAINT "fk_producto_marca" 
FOREIGN KEY ("id_marca") REFERENCES Marcas ("id");

-- Relación entre SubCategorias y Categorias (correcta)
ALTER TABLE SubCategorias ADD CONSTRAINT "fk_subcategoria_categoria" 
FOREIGN KEY ("id_categoria") REFERENCES Categorias ("id");

-- Relación Sucursales -> Empresa
ALTER TABLE Sucursales ADD CONSTRAINT "fk_sucursal_empresa" 
FOREIGN KEY ("id_empresa") REFERENCES Empresa ("id")
ON DELETE RESTRICT ON UPDATE CASCADE;

-- Relación Sucursales -> Ubicaciones
ALTER TABLE Sucursales ADD CONSTRAINT "fk_sucursal_ubicacion" 
FOREIGN KEY ("id_ubicacion") REFERENCES Ubicaciones ("id")
ON DELETE RESTRICT ON UPDATE CASCADE;

-- Relación Usuario-Permisos -> Usuario (CORREGIDO nombre de tabla)
ALTER TABLE PERMISOS_USUARIOS ADD CONSTRAINT "fk_permisosusuario_usuario" 
FOREIGN KEY ("id_usuario") REFERENCES USUARIO ("id")
ON DELETE CASCADE ON UPDATE CASCADE;

-- Relación Usuario-Permisos -> Catálogo de Permisos
ALTER TABLE PERMISOS_USUARIOS ADD CONSTRAINT "fk_permisosusuario_catalogo" 
FOREIGN KEY ("id_catalogo_permiso") REFERENCES CATALOGO_PERMISOS ("id")
ON DELETE CASCADE ON UPDATE CASCADE;

-- Relación SuscripciónUsuario -> Suscripciones (CORREGIDO nombre de tabla)
ALTER TABLE SUBCRIPCION_USUARIO ADD CONSTRAINT "fk_subusuario_subscripcion" 
FOREIGN KEY ("id_subscripcion") REFERENCES SUBSCRIPCIONES ("id")
ON DELETE CASCADE ON UPDATE CASCADE;

-- Relación SuscripciónUsuario -> Usuario
ALTER TABLE SUBCRIPCION_USUARIO ADD CONSTRAINT "fk_subusuario_usuario" 
FOREIGN KEY ("id_usuario") REFERENCES USUARIO ("id")
ON DELETE CASCADE ON UPDATE CASCADE;

-- Relación Publicidades -> Sucursales
ALTER TABLE PUBLICIDADES ADD CONSTRAINT "fk_publicidad_sucursal" 
FOREIGN KEY ("id_sucursal") REFERENCES Sucursales ("id")
ON DELETE CASCADE ON UPDATE CASCADE;

-- Relación EstadísticasPublicidad -> Publicidades
ALTER TABLE ESTADISTICAS_PUBLICIDAD ADD CONSTRAINT "fk_estadisticas_publicidad" 
FOREIGN KEY ("id_publicidad") REFERENCES PUBLICIDADES ("id")
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE producto
ADD COLUMN caracteristicas text null

ALTER TABLE producto
ADD COLUMN caracteristicas_avanzada text null

ALTER TABLE producto
ADD COLUMN views int null

ALTER TABLE subcripcion_usuario
ADD COLUMN creado_por VARCHAR(250) null


