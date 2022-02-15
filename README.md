# audio_python

In this repository I learn different methods in audio proccesing using Python. 
I work with Jupyter notebooks. Some functions and classes in .py files are stored in the algorthims directory.

## Mel spectogram

**1. Introduction**

Python has some awesome libraries for audio processing. Librosa is one of the most popular. Librosa allows read files in different formats. 
We can plot signal spectrum and spectograms. A mel spectrogram is a spectrogram where the frequencies are converted to the mel scale. The Mel scale was created because humans do not perceive frequencies linearly. 

![image](https://user-images.githubusercontent.com/61761700/154109856-742abcbe-9601-414a-91b2-60c31370924f.png)


**2. Technologies**
* Python 3.9
* librosa 0.9.0
* IPython 7.29.0
* matplotlib 3.4.3
## FFT spectrums

**1. Introduction**

There are different ways to calculate Fourier Transform. 
* Discrete Fourier Transform (DFT)
* Fast-Fourier Transform (FFT)

Complexity: 
![image](https://user-images.githubusercontent.com/61761700/154111231-dd7ca63a-e5ad-46b6-84ea-44966bf47846.png)

When N is large enough DFT operation can take very long time.

Fast Fourier transform Algorithms can be implemented using recursion or iteratively.


**2. Technologies**
* Python 3.9
* matplotlib 3.4.3
* numpy 1.20.3
