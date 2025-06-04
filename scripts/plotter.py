from matplotlib import pyplot as plt
import json


model_name = "transformer_denl_config_bpe_smaller_voc"

data_path_bleu = [f"translations/b_{x}.txt" for x in range(1,11)]
data_path_t = [f"b_ts_{x}.txt" for x in range(1,11)]


relative_times = []
sum_time = 0

for i,d in enumerate(data_path_t):

    data = int(open(d).read())

    if i > 1:
        data -= sum_time

    relative_times.append(data)
    sum_time += data

bleu_scores = []

for i,d in enumerate(data_path_bleu):
    
    with open(d, 'r') as file:
        data = json.load(file)

    bleu_scores.append(float(data["score"]))


#plt.plot(bleu_scores, relative_times)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

beam_sizes = [1,2,3,4,5,6,7,8,9,10]

print(bleu_scores)



ax[0].plot(beam_sizes, bleu_scores, marker="o")
ax[0].set_title("Impact of Beam Size on BLEU Score")
ax[0].set_xlabel("Beam Size")
ax[0].set_ylabel("BLEU Score")
ax[0].grid(True)

ax[1].plot(beam_sizes, relative_times, marker="o", color="red")
ax[1].set_title("Impact of Beam Size on Translation Time")
ax[1].set_xlabel("Beam Size")
ax[1].set_ylabel("Time Taken (s)")
ax[1].grid(True)

plt.tight_layout()

plt.savefig("beam_size_impact.png", dpi=300)
plt.show()