-- Script para crear índices optimizados para búsquedas de productos
-- Ejecutar este script en tu base de datos PostgreSQL para mejorar el rendimiento de las búsquedas

-- =====================================================
-- ÍNDICES PARA BÚSQUEDAS DE PRODUCTOS
-- =====================================================

-- 1. Índice para búsquedas por nombre de producto (case-insensitive)
CREATE INDEX IF NOT EXISTS idx_producto_nombre_search 
ON producto USING gin(to_tsvector('spanish', nombre));

-- 2. Índice para búsquedas por descripción (case-insensitive)
CREATE INDEX IF NOT EXISTS idx_producto_descripcion_search 
ON producto USING gin(to_tsvector('spanish', descripcion));

-- 3. Índice compuesto para búsquedas rápidas por nombre y estado activo
CREATE INDEX IF NOT EXISTS idx_producto_nombre_activo 
ON producto (nombre, activo) WHERE activo = 1;

-- 4. Índice para ordenamiento por popularidad (views)
CREATE INDEX IF NOT EXISTS idx_producto_views 
ON producto (views DESC) WHERE activo = 1;

-- 5. Índice para ordenamiento por fecha de creación
CREATE INDEX IF NOT EXISTS idx_producto_created_at 
ON producto (creado DESC) WHERE activo = 1;

-- 6. Índice para ordenamiento por precio
CREATE INDEX IF NOT EXISTS idx_producto_precio 
ON producto (precio_bs) WHERE activo = 1;

-- =====================================================
-- ÍNDICES PARA MARCAS
-- =====================================================

-- 7. Índice para búsquedas por nombre de marca
CREATE INDEX IF NOT EXISTS idx_marcas_nombre_search 
ON marcas USING gin(to_tsvector('spanish', nombre));

-- 8. Índice para búsquedas case-insensitive por nombre de marca
CREATE INDEX IF NOT EXISTS idx_marcas_nombre_lower 
ON marcas (LOWER(nombre));

-- =====================================================
-- ÍNDICES PARA CATEGORÍAS Y SUBCATEGORÍAS
-- =====================================================

-- 9. Índice para búsquedas por nombre de categoría
CREATE INDEX IF NOT EXISTS idx_categorias_nombre_search 
ON categorias USING gin(to_tsvector('spanish', nombre));

-- 10. Índice para búsquedas por nombre de subcategoría
CREATE INDEX IF NOT EXISTS idx_subcategorias_nombre_search 
ON subcategorias USING gin(to_tsvector('spanish', nombre));

-- 11. Índice para relación categoría-subcategoría
CREATE INDEX IF NOT EXISTS idx_subcategorias_categoria_id 
ON subcategorias (id_categoria);

-- =====================================================
-- ÍNDICES PARA EMPRESAS Y SUCURSALES
-- =====================================================

-- 12. Índice para búsquedas por nombre de empresa
CREATE INDEX IF NOT EXISTS idx_empresa_nombre_search 
ON empresa USING gin(to_tsvector('spanish', nombre));

-- 13. Índice para búsquedas case-insensitive por nombre de empresa
CREATE INDEX IF NOT EXISTS idx_empresa_nombre_lower 
ON empresa (LOWER(nombre));

-- 14. Índice para relación sucursal-empresa
CREATE INDEX IF NOT EXISTS idx_sucursales_empresa_id 
ON sucursales (id_empresa);

-- =====================================================
-- ÍNDICES COMPUESTOS PARA BÚSQUEDAS COMPLEJAS
-- =====================================================

-- 15. Índice compuesto para búsquedas por subcategoría y estado activo
CREATE INDEX IF NOT EXISTS idx_producto_subcategoria_activo 
ON producto (id_sub_categoria, activo) WHERE activo = 1;

-- 16. Índice compuesto para búsquedas por sucursal y estado activo
CREATE INDEX IF NOT EXISTS idx_producto_sucursal_activo 
ON producto (id_sucursal, activo) WHERE activo = 1;

-- 17. Índice compuesto para búsquedas por marca y estado activo
CREATE INDEX IF NOT EXISTS idx_producto_marca_activo 
ON producto (id_marca, activo) WHERE activo = 1;

-- =====================================================
-- ÍNDICES PARA BÚSQUEDAS FULL-TEXT AVANZADAS
-- =====================================================

-- 18. Índice full-text compuesto para búsquedas en múltiples campos
CREATE INDEX IF NOT EXISTS idx_producto_fulltext_search 
ON producto USING gin(
    to_tsvector('spanish', 
        COALESCE(nombre, '') || ' ' || 
        COALESCE(descripcion, '') || ' ' ||
        COALESCE(codigo, '')
    )
);

-- =====================================================
-- ESTADÍSTICAS Y ANÁLISIS
-- =====================================================

-- Actualizar estadísticas de la base de datos para optimizar el planificador de consultas
ANALYZE producto;
ANALYZE marcas;
ANALYZE categorias;
ANALYZE subcategorias;
ANALYZE empresa;
ANALYZE sucursales;

-- =====================================================
-- COMENTARIOS PARA DOCUMENTACIÓN
-- =====================================================

COMMENT ON INDEX idx_producto_nombre_search IS 'Índice full-text para búsquedas en nombres de productos';
COMMENT ON INDEX idx_producto_descripcion_search IS 'Índice full-text para búsquedas en descripciones de productos';
COMMENT ON INDEX idx_producto_nombre_activo IS 'Índice compuesto para búsquedas rápidas por nombre en productos activos';
COMMENT ON INDEX idx_producto_views IS 'Índice para ordenamiento por popularidad (vistas)';
COMMENT ON INDEX idx_producto_created_at IS 'Índice para ordenamiento por fecha de creación';
COMMENT ON INDEX idx_producto_precio IS 'Índice para ordenamiento por precio';
COMMENT ON INDEX idx_marcas_nombre_search IS 'Índice full-text para búsquedas en nombres de marcas';
COMMENT ON INDEX idx_categorias_nombre_search IS 'Índice full-text para búsquedas en nombres de categorías';
COMMENT ON INDEX idx_subcategorias_nombre_search IS 'Índice full-text para búsquedas en nombres de subcategorías';
COMMENT ON INDEX idx_empresa_nombre_search IS 'Índice full-text para búsquedas en nombres de empresas';
COMMENT ON INDEX idx_producto_fulltext_search IS 'Índice full-text compuesto para búsquedas avanzadas';

-- =====================================================
-- VERIFICACIÓN DE ÍNDICES CREADOS
-- =====================================================

-- Consulta para verificar que los índices se crearon correctamente
SELECT 
    schemaname,
    tablename,
    indexname,
    indexdef
FROM pg_indexes 
WHERE tablename IN ('producto', 'marcas', 'categorias', 'subcategorias', 'empresa', 'sucursales')
    AND indexname LIKE 'idx_%'
ORDER BY tablename, indexname;
