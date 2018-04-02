{
    'name': 'To-Do Application',
    'description': 'Manage your personal To-Do tasks.',
    'author': 'Daniel Reis',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/todo_access_rules.xml',
        'security/ir.model.access.csv',
        'views/todo_view.xml',
        'views/todo_menu.xml',
    ],
}
