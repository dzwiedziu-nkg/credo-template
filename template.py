from credo_cf import load_json, progress_and_process_image, ID, IMAGE, GRAY
import pandas as pd


# ================= Part 1: How to load data from JSON files ================

# Load from JSON
objects, count, errors = load_json('part_15.json', progress_and_process_image)
print("Load %d detections of cosmic-ray" % count)

# So, in objects[] we have list of dict with attributes:
# objects[0][ID] - id of hits
# objects[0][IMAGE] - numpy array of RGB image (3-dimensions)
# objects[0][GRAY] - numpy array of grayscale image (2-dimensions)
#
# But, we need:
# images[] - list of images as list of numpy array
# and
# ids[] - list of IDs of images from images[]


# Extract images to array of numpy bitmaps and ID to another array:
ids = []
images = []  # RGB image you need if you working on RGB
grays = []  # Grayscale image you need if you working on grayscale only
for o in objects:
    ids.append(o.get(ID))
    images.append(o.get(IMAGE))
    grays.append(o.get(GRAY))


# Alternative: use Pandas:

df = pd.DataFrame(objects)
ids = df[ID].values.tolist()
images = df[IMAGE].values.tolist()
grays = df[GRAY].values.tolist()

# and get all parameters


# Now, the ids[0] have ID for images[0], ids[1] have ID for images[1] and etc.

# ===================== Part 2: implement your algorithm ====================

# ......................... place here your code ----------------------------

results = []  # please append results to `results` list.
classifiers = []  # please append classifier used for achieve the result
# the results[0] should have result for ids[0] using classifiers[0],
# results[1] should have result for ids[1] using  using classifiers[1]
# and etc.

for i in range(0, len(ids)):
    results.append('test_result')
    classifiers.append('test_classifier')

# .................................... end ..................................


# =================== Part 3: save the result in CSV file ===================

# We expect output in CSV file, please do not writing self functions for save
# in CSV. Please use from framework:

df = pd.DataFrame({
    'Classifier': classifiers,
    'Hit ID': ids,
    'Class': results
})

df.to_csv("results.csv", index=False)
