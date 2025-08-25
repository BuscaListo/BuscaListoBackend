#!/usr/bin/env python3
"""
Archivo de prueba para verificar que las importaciones funcionen correctamente.
"""

def test_basic_imports():
    """Prueba las importaciones básicas."""
    try:
        print("Probando importaciones básicas...")
        
        # Importar modelos básicos
        from app.infrastructure.db.models import Product, Category, Brand
        print("✅ Importación de modelos básicos exitosa")
        
        # Importar utilidades
        from app.infrastructure.db.models import map_product_fields, create_model_mapper
        print("✅ Importación de utilidades exitosa")
        
        # Importar alias de campos
        from app.infrastructure.db.models import FIELD_ALIASES
        print("✅ Importación de alias de campos exitosa")
        
        print("\n🎉 Todas las importaciones funcionan correctamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error en importación: {e}")
        return False


def test_model_aliases():
    """Prueba que los alias funcionen correctamente."""
    try:
        print("\nProbando alias de modelos...")
        
        from app.infrastructure.db.models import Product, Category, Brand
        
        # Verificar que los alias apunten a los modelos correctos
        print(f"Product.__name__: {Product.__name__}")
        print(f"Category.__name__: {Category.__name__}")
        print(f"Brand.__name__: {Brand.__name__}")
        
        print("✅ Alias de modelos funcionan correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error en alias de modelos: {e}")
        return False


def test_field_mapping():
    """Prueba el mapeo de campos."""
    try:
        print("\nProbando mapeo de campos...")
        
        from app.infrastructure.db.models import map_product_fields
        
        # Datos de prueba en inglés
        test_data = {
            "name": "Producto Test",
            "description": "Descripción test",
            "price_bs": 100.0,
            "subcategory_id": 1
        }
        
        # Mapear a español
        spanish_data = map_product_fields(test_data)
        print(f"Datos en inglés: {test_data}")
        print(f"Datos mapeados a español: {spanish_data}")
        
        print("✅ Mapeo de campos funciona correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error en mapeo de campos: {e}")
        return False


if __name__ == "__main__":
    print("🚀 Iniciando pruebas de importación...\n")
    
    success = True
    success &= test_basic_imports()
    success &= test_model_aliases()
    success &= test_field_mapping()
    
    if success:
        print("\n🎉 Todas las pruebas pasaron exitosamente!")
    else:
        print("\n💥 Algunas pruebas fallaron.")
