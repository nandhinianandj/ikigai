
import io
import venn
import matplotlib.pyplot as plt
from collections import ChainMap

def draw(data):
    values = list(data.items())
    print(values)
    set_labels = ['Get Paid For', 'World Needs', 'You Love', 'You are good at']
    #Import libraries
    encodings, rev_encodings = venn.get_str_labels(values)
    
    fig, ax = venn.ikigai_venn4(dict(zip(set_labels,encodings.values())), names=set_labels, figsize=(16,16),
                            rev_encs = rev_encodings,
                            venn_type='circle', enc_type='encoding',)
    plt.title("My Ikigai");
    
    plt.savefig('ikigai.png', format='png')
    plt.show()
    
    #set_colors=('r', 'g','purple', 'skyblue'), alpha = 0.7);)
