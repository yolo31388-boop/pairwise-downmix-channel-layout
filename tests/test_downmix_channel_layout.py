import pytest
import media.downmix_channel_layout as mod

CASES = [
    ("layout_coeff", (1,)),
    ("lfe_lowpass_limiter", (1,)),
    ("surround_decorrelate", (1,)),
    ("channel_map", (1,)),
    ("delay_align", (1,)),
    ("determinism", (1,)),
    ("peak_normalize", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("metadata_layout", (1,)),
    ("metrics", (1,)),
    ("downmix", (1,)),
    ("stereo_out", (1,)),
    ("gain_match", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
