import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def LIBROSA_LOAD(data):
    y,sr = librosa.load(data,sr = None)
    
    return y,sr
    
def TWO_PLOT_TIME_DOMAIN(signal1,signal2):
    y_1,sr = LIBROSA_LOAD(signal1)
    y_2,sr = LIBROSA_LOAD(signal2)

    fig, ax = plt.subplots(nrows=2, sharex=True, sharey=True)
    librosa.display.waveshow(y_1, sr=sr, ax=ax[0])
    ax[0].set(title='Time domain plot of {}'.format(signal1))
    ax[0].label_outer()

    librosa.display.waveshow(y_2, sr=sr, ax=ax[1])
    ax[1].set(title='Time domain plot of {}'.format(signal2))
    plt.plot()

    # Render the Matplotlib figure in Streamlit
    st.pyplot(fig)


def DIFF_TWO_PLOT_TIME_DOMAIN(y_1,sr_1,y_2,sr_2):
    #y_1,sr = LIBROSA_LOAD(signal1)
    #y_2,sr = LIBROSA_LOAD(signal2)

    fig, ax = plt.subplots(nrows=2, sharex=True, sharey=True)
    librosa.display.waveshow(y_1, sr=sr_1, ax=ax[0])
    ax[0].set(title='Time domain plot of Expert')
    ax[0].label_outer()

    librosa.display.waveshow(y_2, sr=sr_2, ax=ax[1])
    ax[1].set(title='Time domain plot of  Learner')
    plt.plot()

    # Render the Matplotlib figure in Streamlit
    st.pyplot(fig)

def TWO_PLOT_MEL_SPECTROGRAM(signal1,signal2):
    # Load the first audio file and compute its mel spectrogram
    y1,sr1 = LIBROSA_LOAD(signal1)
    y2,sr2 = LIBROSA_LOAD(signal2)
    
    #y1, sr1 = librosa.load(signal1)
    S1 = librosa.feature.melspectrogram(y = y1, sr=sr1)

    # Load the second audio file and compute its mel spectrogram
    #y2, sr2 = librosa.load(signal2)
    S2 = librosa.feature.melspectrogram(y = y2, sr=sr2)

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))

    # Plot the first mel spectrogram on the first subplot
    img1 = librosa.display.specshow(librosa.power_to_db(S1, ref=np.max), y_axis='mel', x_axis='time', ax=ax1, cmap='viridis')
    ax1.set(title='Mel Spectrogram of {}'.format(signal1))
    #ax1.set_title('Mel spectrogram of audio file 1')
    fig.colorbar(img1, ax=ax1, format='%+2.0f dB')

    # Plot the second mel spectrogram on the second subplot
    img2 = librosa.display.specshow(librosa.power_to_db(S2, ref=np.max), y_axis='mel', x_axis='time', ax=ax2, cmap='viridis')
    #ax2.set_title('Mel spectrogram of audio file 2')
    ax2.set(title='Mel Spectrogram of {}'.format(signal2))
    fig.colorbar(img2, ax=ax2, format='%+2.0f dB')

    # Adjust the layout of the subplots
    plt.tight_layout()

    # Show the plot
    #plt.show()
    st.pyplot(fig)



def DIFF_TWO_PLOT_MEL_SPECTROGRAM(y1, sr1, y2, sr2):
    # Load the first audio file and compute its mel spectrogram
    # y1,sr1 = LIBROSA_LOAD(signal1)
    # y2,sr2 = LIBROSA_LOAD(signal2)
    
    #y1, sr1 = librosa.load(signal1)
    S1 = librosa.feature.melspectrogram(y = y1, sr=sr1)

    # Load the second audio file and compute its mel spectrogram
    #y2, sr2 = librosa.load(signal2)
    S2 = librosa.feature.melspectrogram(y = y2, sr=sr2)

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))

    # Plot the first mel spectrogram on the first subplot
    img1 = librosa.display.specshow(librosa.power_to_db(S1, ref=np.max), y_axis='mel', x_axis='time', ax=ax1, cmap='viridis')
    ax1.set(title='Mel Spectrogram of Expert')
    #ax1.set_title('Mel spectrogram of audio file 1')
    fig.colorbar(img1, ax=ax1, format='%+2.0f dB')

    # Plot the second mel spectrogram on the second subplot
    img2 = librosa.display.specshow(librosa.power_to_db(S2, ref=np.max), y_axis='mel', x_axis='time', ax=ax2, cmap='viridis')
    #ax2.set_title('Mel spectrogram of audio file 2')
    ax2.set(title='Mel Spectrogram of Learner')
    fig.colorbar(img2, ax=ax2, format='%+2.0f dB')

    # Adjust the layout of the subplots
    plt.tight_layout()

    # Show the plot
    #plt.show()
    st.pyplot(fig)


st.set_page_config(
    page_title="Hello Carnatic Music",
    page_icon="👋",
)

st.write("# Drop your files here! 👋")



# Streamlit app
#st.title('Audio Signal Visualization')

# File upload
uploaded_file_T = st.file_uploader('Upload an audio file lvl Expert', type=['mp3'])

uploaded_file_S = st.file_uploader('Upload an audio file lvl learner', type=['mp3'])

# signal_T = uploaded_file_T

# signal_S = uploaded_file_S



# Assuming you have the audio data in `y` and the sample rate in `sr`

#output_path_T = 'data/output_teacher.wav'  # Specify the output file path
#output_path_S = 'data/output_student.wav'
# Convert and save the audio file
#librosa.output.write_wav(output_path, y, sr)


if uploaded_file_T is not None:
    if uploaded_file_S is not None:
        y_1, sr_1 = LIBROSA_LOAD(uploaded_file_T)
        y_2, sr_2 = LIBROSA_LOAD(uploaded_file_S)
        #librosa.output.write_wav(output_path_T, y_1, sr_1)
        #librosa.output.write_wav(output_path_S, y_2, sr_2)
        #st.write(y_1,y_2)
        #st.write("Done")
        st.title('Audio Signal Visualization Time Domain')
        # TWO_PLOT_T(uploaded_file_T,uploaded_file_S)
        DIFF_TWO_PLOT_TIME_DOMAIN(y_1,sr_1,y_2,sr_2)

        st.title('Audio Signal Visualization Frequency Domain')
        DIFF_TWO_PLOT_MEL_SPECTROGRAM(y_1,sr_1,y_2,sr_2)

        




        # st.title('Audio Signal Visualization Time Domain')
        # TWO_PLOT_T(uploaded_file_T,uploaded_file_S)



        # st.title('Audio Signal Visualization Frequency Domain')
        # TWO_PLOT_MEL_SPECTROGRAM(uploaded_file_T,uploaded_file_S)

        




# if uploaded_file_T is not None:
#     if uploaded_file_S is not None:
#         st.title('Audio Signal Visualization Time Domain')
        #TWO_PLOT_T(uploaded_file_T,uploaded_file_S)

        #st.title('Audio Signal Visualization Frequency Domain')
        #TWO_PLOT_MEL_SPECTROGRAM(uploaded_file_T,uploaded_file_S)


         #TWO_PLOT_MEL_SPECTROGRAM(uploaded_file_T,uploaded_file_S)


# if signal_T is not None:
#     if signal_S is not None:
#         st.title('Audio Signal Visualization Frequency Domain')
#         #TWO_PLOT_TIME_DOMAIN(uploaded_file_T,uploaded_file_S)
#         TWO_PLOT_MEL_SPECTROGRAM(signal_T,signal_S)


# if uploaded_file_T is not None:
#     if uploaded_file_S is not None:
#         TWO_PLOT_MEL_SPECTROGRAM(uploaded_file_T,uploaded_file_S)



# for i,j in zip(uploaded_file_T,uploaded_file_S):
#     if i is not None and  j is not None:
#         TWO_PLOT_TIME_DOMAIN(i,j)

# if uploaded_file_T is not None:
#     audio_data, sr = librosa.load(uploaded_file_T, sr=None)
#     plot_audio_signal(audio_data, sr)

    
# if uploaded_file_S is not None:
#     audio_data, sr = librosa.load(uploaded_file_S, sr=None)
#     plot_audio_signal(audio_data, sr)








