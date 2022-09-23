from pywebio.input import *
from pywebio.output import *
import time
from pywebio.pin import * 
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
import numpy as np
import matplotlib.pyplot as plt 
import argparse
from pywebio import start_server
app = Flask(__name__)



def chisquare():
    with use_scope('scope2', clear=True):
        points = input_group("Select points", [
            input('Starting point', name = 'starting_point', required = True, type=NUMBER),
            input('Ending point', name = 'ending_point', required = True, type=NUMBER)
            ])

        x = np.linspace(points['starting_point'], points['ending_point'], 100)
        y = x**2
        plot(x,y,'tmpsquare.png')
        put_buttons(['Plot'], onclick=[plot_chisquare])

def plot_chisquare():
    with use_scope('scope2'):
        put_image(open('tmpsquare.png', 'rb').read())
        toast('Click to save figure', position='right', color='#2188ff', duration=0, onclick=save_chisquare)

def chicube():
    with use_scope('scope2', clear=True):
        points = input_group("Select points", [
            input('Starting point', name = 'starting_point', required = True, type=NUMBER),
            input('Ending point', name = 'ending_point', required = True, type=NUMBER)
            ])
        x = np.linspace(points['starting_point'], points['ending_point'], 100)
        y = x**2
        plot(x,y,'tmpcube.png')
        put_buttons(['Plot'], onclick=[plot_chicube])

def plot_chicube():
    with use_scope('scope2'):
        put_image(open('tmpcube.png', 'rb').read())
        toast('Click to save figure', position='right', color='#2188ff', duration=0, onclick=save_chicube)

def save_chicube():
    with use_scope('scope2'):
        put_processbar('bar');
        for i in range(1, 11):
            set_processbar('bar', i / 10)
            time.sleep(0.1)
        put_file('chi-cube-plot.png', open('tmpcube.png', 'rb').read(), 'download chi-cube-plot')

def save_chisquare():
    with use_scope('scope2'):
        put_processbar('bar');
        for i in range(1, 11):
            set_processbar('bar', i / 10)
            time.sleep(0.1)
        put_file('chi-square-plot.png', open('tmpsquare.png', 'rb').read(), 'download chi-square-plot')

def plot(x,y,name):
    plt.plot(x,y)
    plt.title('Some plot')
    plt.savefig(name)
    plt.close()




def main():
    with use_scope('main_scope'):
        put_image('https://www.ballista.com/wp-content/uploads/2022/03/Picture1.jpg')
        put_markdown(r""" # Chi square and cube  demo.
        In this demo you are asked to select an interval to compute and plot the chi square and the chi cube functions. 
        """)
        put_buttons(['Chi square', 'Chi cube'], onclick = [chisquare, chicube])


app.add_url_rule('/tool','webio_view', webio_view(main),
   methods=['GET', 'POST', 'OPTIONS'])
# main()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port",type=int, default=8080)
    args = parser.parse_args()

    start_server(main, port=args.port)