/**@odoo-module **/
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { patch } from "@web/core/utils/patch";

patch(ControlButtons.prototype, {
    get buttonClass() {
        return "btn btn-light btn-lg flex-shrink-0 ms-2";
    },
    
    async clickPrintBill() {
        const order = this.pos.get_order();
        if (order && order.get_orderlines().length > 0) {
            // Usar la funcionalidad nativa de impresión de Odoo POS
            await this.pos.printReceipt();
        }
    },
});