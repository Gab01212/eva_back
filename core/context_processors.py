def contador_canasta(request):
    canasta = request.session.get('canasta', {})
    total_items = sum(item['cantidad'] for item in canasta.values())
    return {'contador_canasta': total_items}