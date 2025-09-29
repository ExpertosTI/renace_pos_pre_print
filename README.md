# POS Pre Impresión

Módulo de Odoo para pre-impresión de recibos en punto de venta minorista.

## Descripción

Permite imprimir una pre-cuenta en el punto de venta minorista similar al punto de venta tipo restaurante.

## Instalación

1. Copia el módulo a tu directorio de addons de Odoo 18.0
2. Actualiza la lista de módulos: `Apps > Update Apps List`
3. Busca "Botón de Impresión de Factura POS" e instala el módulo

## Uso

Una vez instalado:
1. Ve al **Punto de Venta**
2. Agrega productos a una orden
3. Verás el botón **"Cuenta"** con ícono de Impresora
4. Haz clic para imprimir la cuenta/recibo

## Dependencias

- `base`
- `point_of_sale`

## Compatibilidad

- **Odoo 18.0**
- Versiones anteriores (usar rama correspondiente)

## Estructura del Módulo

```
renace_pos_pre_print/
├── __manifest__.py          # Configuración del módulo
├── __init__.py             # Inicialización
├── static/
│   └── src/
│       ├── js/
│       │   └── pos_print_bill_button.js    # Lógica JavaScript
│       └── xml/
│           └── pos_print_bill_button.xml   # Template del botón
└── README.md
```

## Changelog

### Version 18.0.0.1
- **Migración a Odoo 18.0**
- **Traducción completa al español**
- **Funcionalidad de Impresión real implementada**
- **Interfaz actualizada para Odoo 18.0**

## Licencia

OPL-1

## Autor

**Adderly Marte**  
Website: [renace.tech](https://renace.tech)

---

*Desarrollado por renace.tech para Odoo 18.0*
- **Email:** adderlymarte@renace.tech

---

© 2024 RENACE.TECH - Todos los derechos reservados