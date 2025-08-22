CREATE TABLE producto (
  id BIGSERIAL PRIMARY KEY,
  nombre VARCHAR NOT NULL,
  descripcion TEXT,
  precio_bs DOUBLE PRECISION NOT NULL,
  precio_dls DOUBLE PRECISION,
  imagenes TEXT,
  codigo VARCHAR(150),
  in_stock SMALLINT NOT NULL DEFAULT 1 CHECK (in_stock IN (0,1)),
  id_sub_categoria BIGINT NOT NULL,
  id_sucursal BIGINT NOT NULL,
  id_marca BIGINT NOT NULL,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(250),
  activo SMALLINT NOT NULL DEFAULT 1 CHECK (activo IN (0,1))
);

CREATE TABLE categorias (
  id BIGSERIAL PRIMARY KEY,
  nombre VARCHAR NOT NULL,
  imagenes TEXT,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE subcategorias (
  id BIGSERIAL PRIMARY KEY,
  nombre VARCHAR NOT NULL,
  imagenes TEXT,
  id_categoria BIGINT NOT NULL,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE stock (
  id BIGSERIAL PRIMARY KEY,
  id_producto BIGINT NOT NULL,
  cantidad_total INTEGER,
  cantidad_vendida INTEGER,
  cantidad_ofertada INTEGER,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE marcas (
  id BIGSERIAL PRIMARY KEY,
  nombre VARCHAR NOT NULL,
  descripcion TEXT,
  imagenes TEXT,
  logo TEXT,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE ofertas (
  id BIGSERIAL PRIMARY KEY,
  descripcion TEXT NOT NULL,
  porcentaje DECIMAL(5,2),
  id_producto BIGINT,
  id_categoria BIGINT,
  id_sub_categoria BIGINT,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE sucursales (
  id BIGSERIAL PRIMARY KEY,
  nombre VARCHAR NOT NULL,
  imagenes TEXT,
  id_empresa BIGINT NOT NULL,
  id_ubicacion BIGINT NOT NULL,
  id_usuario BIGINT NOT NULL,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE empresa (
  id BIGSERIAL PRIMARY KEY,
  nombre VARCHAR NOT NULL,
  telefono VARCHAR(20),
  id_ubicacion BIGINT NOT NULL,
  logo TEXT,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE ubicaciones (
  id BIGSERIAL PRIMARY KEY,
  nombre VARCHAR NOT NULL,
  latitud DECIMAL(10,8) NOT NULL,
  longitud DECIMAL(10,8) NOT NULL,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE webservice_log (
  id BIGSERIAL PRIMARY KEY,
  id_web_service BIGINT NOT NULL,
  input TEXT,
  error TEXT,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255)
);

CREATE TABLE web_service (
  id BIGSERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  descripcion VARCHAR(255),
  url VARCHAR(255),
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE bitacora_precio_producto (
  id BIGSERIAL PRIMARY KEY,
  id_producto BIGINT NOT NULL,
  precio_actualizado DECIMAL(10,2),
  precio_nuevo DECIMAL(10,2),
  porcentaje DECIMAL(5,2),
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255)
);

CREATE TABLE catalogo_permisos (
  id BIGSERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE permisos_usuarios (
  id BIGSERIAL PRIMARY KEY,
  id_usuario BIGINT,
  id_catalogo_permiso BIGINT,
  read BOOLEAN DEFAULT FALSE,
  write BOOLEAN DEFAULT FALSE,
  delete BOOLEAN DEFAULT FALSE,
  edit BOOLEAN DEFAULT FALSE,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE subscripciones (
  id BIGSERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  precio DECIMAL(10,2),
  anuncios BOOLEAN DEFAULT FALSE,
  prioridad_listado BOOLEAN DEFAULT FALSE,
  ubicaciones BOOLEAN DEFAULT FALSE,
  estadisticas BOOLEAN DEFAULT FALSE,
  soporte BOOLEAN DEFAULT FALSE,
  extras BOOLEAN DEFAULT FALSE,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE imagenes (
  id BIGSERIAL PRIMARY KEY,
  url VARCHAR(150),
  id_producto BIGINT,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE subscripcion_usuario (
  id BIGSERIAL PRIMARY KEY,
  id_subscripcion BIGINT NOT NULL,
  id_usuario BIGINT NOT NULL,
  activo BOOLEAN DEFAULT TRUE,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE usuario (
  id BIGSERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  email VARCHAR(255) UNIQUE,
  password VARCHAR(255),
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE publicidades (
  id BIGSERIAL PRIMARY KEY,
  id_sucursal BIGINT NOT NULL,
  imagenes_publicidad TEXT,
  link_destino VARCHAR(300),
  prioridad INTEGER,
  fecha_inicio DATE,
  fecha_fin DATE,
  activo BOOLEAN DEFAULT TRUE,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE estadisticas_publicidad (
  id BIGSERIAL PRIMARY KEY,
  id_publicidad BIGINT,
  impresiones INTEGER,
  clics INTEGER,
  fecha DATE,
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE monedas (
  id BIGSERIAL PRIMARY KEY,
  divisa VARCHAR(150),
  precio_bs DECIMAL(10,2),
  creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  creado_por VARCHAR(255),
  activo BOOLEAN DEFAULT TRUE
);

-- FKs
ALTER TABLE imagenes ADD CONSTRAINT fk_imagenes_producto FOREIGN KEY (id_producto) REFERENCES producto(id);
ALTER TABLE producto ADD CONSTRAINT fk_producto_subcategoria FOREIGN KEY (id_sub_categoria) REFERENCES subcategorias(id);
ALTER TABLE producto ADD CONSTRAINT fk_producto_sucursal FOREIGN KEY (id_sucursal) REFERENCES sucursales(id);
ALTER TABLE producto ADD CONSTRAINT fk_producto_marca FOREIGN KEY (id_marca) REFERENCES marcas(id);
ALTER TABLE subcategorias ADD CONSTRAINT fk_subcategoria_categoria FOREIGN KEY (id_categoria) REFERENCES categorias(id);
ALTER TABLE sucursales ADD CONSTRAINT fk_sucursal_empresa FOREIGN KEY (id_empresa) REFERENCES empresa(id) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE sucursales ADD CONSTRAINT fk_sucursal_ubicacion FOREIGN KEY (id_ubicacion) REFERENCES ubicaciones(id) ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE permisos_usuarios ADD CONSTRAINT fk_permisosusuario_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE permisos_usuarios ADD CONSTRAINT fk_permisosusuario_catalogo FOREIGN KEY (id_catalogo_permiso) REFERENCES catalogo_permisos(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE subscripcion_usuario ADD CONSTRAINT fk_subusuario_subscripcion FOREIGN KEY (id_subscripcion) REFERENCES subscripciones(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE subscripcion_usuario ADD CONSTRAINT fk_subusuario_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE publicidades ADD CONSTRAINT fk_publicidad_sucursal FOREIGN KEY (id_sucursal) REFERENCES sucursales(id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE estadisticas_publicidad ADD CONSTRAINT fk_estadisticas_publicidad FOREIGN KEY (id_publicidad) REFERENCES publicidades(id) ON DELETE CASCADE ON UPDATE CASCADE;

-- Nuevas columnas
ALTER TABLE producto ADD COLUMN caracteristicas TEXT NULL;
ALTER TABLE producto ADD COLUMN caracteristicas_avanzada TEXT NULL;
ALTER TABLE producto ADD COLUMN views INT NULL;
ALTER TABLE subscripcion_usuario ADD COLUMN creado_por VARCHAR(250) NULL;

-- Modificaciones columnas
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
