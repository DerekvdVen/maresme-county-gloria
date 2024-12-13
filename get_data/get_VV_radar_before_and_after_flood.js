// The data input is from COPERNICUS/S1_GRD
// You can set your own geometry but I chose north = 41.70, south = 41.63, east = 2.81, west = 2.67

function despeckle(img) {
  return img
    .focalMean(30, "square", "meters")
    .copyProperties(img, img.propertyNames());
}

Map.centerObject(geometry);

var before_flood_start = "2020-01-01";
var before_flood_end = "2020-01-19";

var flood_start = "2020-01-19";
var flood_end = "2020-01-25";

var after = imageCollection
  .filterDate(flood_start, flood_end)
  .filterBounds(geometry)
  .filter(ee.Filter.listContains("transmitterReceiverPolarisation", "VV")) //VV for water
  .filter(ee.Filter.eq("instrumentMode", "IW"))
  // .filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))
  .select("VV")
  .map(despeckle)
  .min();

var before = imageCollection
  .filterDate(before_flood_start, before_flood_end)
  .filterBounds(geometry)
  .filter(ee.Filter.listContains("transmitterReceiverPolarisation", "VV")) //VV for water
  .filter(ee.Filter.eq("instrumentMode", "IW"))
  // .filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))
  .select("VV")
  .map(despeckle)
  .min();

Map.addLayer(before.clip(geometry), [], "before", false);
Map.addLayer(after.clip(geometry), [], "after", false);

var change = before.subtract(after);
Map.addLayer(change.clip(geometry), [], "flooded_region", false);

print(ui.Chart.image.histogram(change, geometry, 30));

Map.addLayer(change.gt(1).clip(geometry), [], "masked", false);

// Set 0s to NaN
var flood_threshold = change.gt(1);
var flood_mask = flood_threshold.updateMask(flood_threshold);

var flood_area = flood_mask.multiply(ee.Image.pixelArea().divide(1e6));
var flood_area_region = flood_area
  .reduceRegion({
    reducer: ee.Reducer.sum(),
    geometry: geometry,
    scale: 100,
  })
  .values()
  .get(0);

print("area of flooded region (km2): ", ee.Number(flood_area_region));

Export.image.toDrive({
  image: before.clip(geometry),
  description: "Before_Flood",
  folder: "EarthEngineExports", // Optional: Folder in your Google Drive
  scale: 30,
  region: geometry,
  fileFormat: "GeoTIFF",
});

// Export 'after' image as GeoTIFF
Export.image.toDrive({
  image: after.clip(geometry),
  description: "After_Flood",
  folder: "EarthEngineExports", // Optional: Folder in your Google Drive
  scale: 30,
  region: geometry,
  fileFormat: "GeoTIFF",
});

// Export 'change' image as GeoTIFF
Export.image.toDrive({
  image: change.clip(geometry),
  description: "Flood_Change",
  folder: "EarthEngineExports", // Optional: Folder in your Google Drive
  scale: 30,
  region: geometry,
  fileFormat: "GeoTIFF",
});

var featureCollection = ee.FeatureCollection([ee.Feature(geometry)]);

// Export the geometry as a GeoJSON file to Google Drive
Export.table.toDrive({
  collection: featureCollection,
  description: "ExportedGeometry",
  folder: "EarthEngineExports", // Folder in Google Drive
  fileNamePrefix: "geometry_export",
  fileFormat: "GeoJSON",
});
