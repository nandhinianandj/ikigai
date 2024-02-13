import io
import venn
import matplotlib.pyplot as plt
from collections import ChainMap


values = [['Systems Design', 'Coding/SW_Engineering'],
          ['Writing','Connecting With People','Play Bass Guitar', 'Teach Philosophy Alignment',
              'Systems Design', 'Coding/SW_Engineering', 'Making People Laugh'],
          ['Play badminton', 'Running', 'Reading', 'Dance', 'Making People Laugh'],
          ['Write Poetry','Teach Philosophy Alignment', 'Systems Design', 'Connecting with people',
           'Writing', 'Coding/SW_Engineering', 'Dance', 'Making People Laugh','Reading','Running',
           'Play Badminton']
          ]
def draw_ikigai(subject, inputs):
    #Import libraries
    encodings, rev_encodings = venn.get_str_labels(values)
    set_labels = ['Get Paid For', 'World Needs', 'You Love', 'You are good at']
    
    fig, ax = venn.ikigai_venn4(dict(zip(set_labels,encodings.values())), names=set_labels, figsize=(16,16),
                            rev_encs = rev_encodings,
                            venn_type='circle', enc_type='encoding',)
    plt.title("My Ikigai");
    
    img_buf = io.BytesIO()
    plt.savefig('{}_ikigai.png'.format(subject), format='png')
