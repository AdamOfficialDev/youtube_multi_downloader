# Versi Lama
# import pytube

# def format_size(size_in_bytes):
#     # Konversi ukuran dalam bytes menjadi ukuran yang lebih mudah dibaca
#     size_in_bytes = int(size_in_bytes)
#     size_units = ["B", "KB", "MB", "GB", "TB"]

#     index = 0
#     while size_in_bytes >= 1024 and index < len(size_units) - 1:
#         size_in_bytes /= 1024
#         index += 1

#     return f"{size_in_bytes:.2f} {size_units[index]}"

# def download_video(url, download_path):
#     youtube = pytube.YouTube(url)
#     video_streams = youtube.streams.filter(progressive=True)

#     # Menampilkan pilihan resolusi video yang tersedia
#     print("Pilih Resolusi Video:")
#     for i, stream in enumerate(video_streams):
#         print(f"{i+1}. Resolusi: {stream.resolution}, Format: {stream.mime_type}, Ukuran: {format_size(stream.filesize)}")

#     choice = int(input("Masukkan pilihan resolusi (angka): "))
#     selected_stream = video_streams[choice-1]

#     # Mendapatkan informasi video
#     title = selected_stream.title
#     author = youtube.author
#     duration = youtube.length
#     views = youtube.views
#     rating = youtube.rating
#     video_resolution = f"{selected_stream.resolution}p"
#     video_size = format_size(selected_stream.filesize)

#     # Menampilkan informasi video
#     print("Informasi Video:")
#     print("Judul:", title)
#     print("Penulis:", author)
#     print("Durasi:", duration, "detik")
#     print("Jumlah Tampilan:", views)
#     print("Rating:", rating)
#     print("Resolusi Video:", video_resolution)
#     print("Ukuran Video:", video_size)

#     confirm_choice = input("Apakah Anda ingin mengunduh video ini? (y/n): ")

#     if confirm_choice.lower() == 'y':
#         # Mendownload video ke direktori yang ditentukan
#         print("Mengunduh video...")
#         selected_stream.download(download_path)
#         print("Unduhan selesai!")

#     else:
#         print("Unduhan dibatalkan.")

# def download_playlist(url, download_path):
#     playlist = pytube.Playlist(url)

#     # Mendapatkan informasi playlist
#     playlist_title = playlist.title
#     playlist_length = len(playlist.video_urls)

#     # Menampilkan informasi playlist
#     print("Judul Playlist:", playlist_title)
#     print("Jumlah Video:", playlist_length)

#     choice = input("Apakah Anda ingin mengunduh semua video dalam playlist ini? (y/n): ")

#     if choice.lower() == 'y':
#         for video_url in playlist.video_urls:
#             download_video(video_url, download_path)
#             print()

#     else:
#         print("Unduhan playlist dibatalkan.")

# def main():
#     print("=== PROGRAM PENGUNDUH VIDEO YOUTUBE ===")

#     # Memasukkan direktori tujuan penyimpanan
#     download_path = r"C:\Users\Adam  IPTEK\Videos"

#     while True:
#         print("\nPilih opsi:")
#         print("1. Unduh video")
#         print("2. Unduh playlist")
#         print("0. Keluar")

#         choice = input("Masukkan pilihan Anda: ")

#         if choice == '1':
#             url = input("Masukkan URL video YouTube: ")
#             download_video(url, download_path)

#         elif choice == '2':
#             url = input("Masukkan URL playlist YouTube: ")
#             download_playlist(url, download_path)

#         elif choice == '0':
#             break

#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.")

# if __name__ == '__main__':
#     main()

# Yang Baru

import pytube

def format_size(size_in_bytes):
    # Konversi ukuran dalam bytes menjadi ukuran yang lebih mudah dibaca
    size_in_bytes = int(size_in_bytes)
    size_units = ["B", "KB", "MB", "GB", "TB"]

    index = 0
    while size_in_bytes >= 1024 and index < len(size_units) - 1:
        size_in_bytes /= 1024
        index += 1

    return f"{size_in_bytes:.2f} {size_units[index]}"

def download_video(url, download_path):
    youtube = pytube.YouTube(url)
    video_streams = youtube.streams.filter(progressive=True)

    # Menampilkan pilihan resolusi video yang tersedia
    print("Pilih Resolusi Video:")
    for i, stream in enumerate(video_streams):
        print(f"{i+1}. Resolusi: {stream.resolution}, Format: {stream.mime_type}, Ukuran: {format_size(stream.filesize)}")

    choice = int(input("Masukkan pilihan resolusi (angka): "))
    selected_stream = video_streams[choice-1]

    # Mendapatkan informasi video
    title = selected_stream.title
    author = youtube.author
    duration = youtube.length
    views = youtube.views
    rating = youtube.rating
    video_resolution = f"{selected_stream.resolution}p"
    video_size = format_size(selected_stream.filesize)

    # Menampilkan informasi video
    print("Informasi Video:")
    print("Judul:", title)
    print("Penulis:", author)
    print("Durasi:", duration, "detik")
    print("Jumlah Tampilan:", views)
    print("Rating:", rating)
    print("Resolusi Video:", video_resolution)
    print("Ukuran Video:", video_size)

    confirm_choice = input("Apakah Anda ingin mengunduh video ini? (y/n): ")

    if confirm_choice.lower() == 'y':
        # Mendownload video ke direktori yang ditentukan
        print("Mengunduh video...")
        selected_stream.download(download_path)
        print("Unduhan selesai!")

    else:
        print("Unduhan dibatalkan.")

def download_playlist(url, download_path):
    playlist = pytube.Playlist(url)

    # Mendapatkan informasi playlist
    playlist_title = playlist.title
    playlist_length = len(playlist.video_urls)

    # Menampilkan informasi playlist
    print("Judul Playlist:", playlist_title)
    print("Jumlah Video:", playlist_length)

    choice = input("Apakah Anda ingin mengunduh semua video dalam playlist ini? (y/n): ")

    if choice.lower() == 'y':
        for video_url in playlist.video_urls:
            youtube = pytube.YouTube(video_url)
            video_streams = youtube.streams.filter(progressive=True)
            selected_stream = video_streams.first()

            # Mendapatkan informasi video
            title = selected_stream.title
            video_size = format_size(selected_stream.filesize)

            # Menampilkan informasi video
            print("\nInformasi Video:")
            print("Judul:", title)
            print("Ukuran Video:", video_size)

            confirm_choice = input("Apakah Anda ingin mengunduh video ini? (y/n): ")

            if confirm_choice.lower() == 'y':
                # Mendownload video ke direktori yang ditentukan
                print("Mengunduh video...")
                selected_stream.download(download_path)
                print("Unduhan selesai!")
            else:
                print("Unduhan dibatalkan.")
    else:
        print("Unduhan playlist dibatalkan.")

def main():
    print("=== PROGRAM PENGUNDUH VIDEO YOUTUBE ===")

    # Memasukkan direktori tujuan penyimpanan
    download_path = r"C:\Users\Adam  IPTEK\Videos"

    while True:
        print("\nPilih opsi:")
        print("1. Unduh video")
        print("2. Unduh playlist")
        print("0. Keluar")

        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            url = input("Masukkan URL video YouTube: ")
            download_video(url, download_path)

        elif choice == '2':
            url = input("Masukkan URL playlist YouTube: ")
            download_playlist(url, download_path)

        elif choice == '0':
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()
