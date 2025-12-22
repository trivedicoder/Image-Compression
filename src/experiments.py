from ea_compression import evolve
from baseline import baseline_resize
from metrics import ssim_score


def run(original):
    baseline = baseline_resize(original)
    best, history = evolve(original)

    print("Baseline SSIM:", ssim_score(baseline, original))
    print("EA SSIM:", ssim_score(best, original))

    return baseline, best, history

#Lol