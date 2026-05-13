import folium

m = folium.Map(
    location=[11.7058, -70.1857],
    zoom_start=13,
    tiles="http://localhost:9000/tiles_local/{z}/{x}/{y}.png",
    attr="OpenStreetMap",
    min_zoom=10,
    max_zoom=16
)

m.save("eppaaa.html")
print("✅ Listo!")