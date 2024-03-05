{
    'name' : 'Transport Management System',
    'version' : '1.0',
    'category': '',
    'summary' : 'Track Tranportation of Vehicles',
    'depends' : [
        'fleet','stock_picking_batch'
    ],
    'data' : [
        'security/ir.model.access.csv',

        'views/fleet_vehicle_model_category_views.xml',
        'views/stock_picking_batch_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'auto-install': True,
}
