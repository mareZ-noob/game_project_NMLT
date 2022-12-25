> Đồ án Nhập môn lập trình làm game (hứng táo) khi speed run pygame 1 tuần.

# Catching Apple

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [How to play](#how-to-play)

## General info
Recommend running this project in Pycharm.
	
## Technologies 

Project is created with:
* Pycharm version: 2022.2
* Python version: 3.10
* Pygame version: 2.1.2
	
## Setup

To run this project in Pycharm:

### First, in terminal, install Pygame via:
```
pip install pygame
```

### Second, in terminal, run this project via:
```
python menu.py
```

## How to play

### Hướng dẫn chơi game: Menu cơ bản của game gầm 4 nút là Play, Background, Setting và Quit.

- Nút Quit: Sau khi nhấn thì sẽ thoát khỏi game ngay lập tức.
- Nút Setting: Sau khi nhấn sẽ chuyển đến phần chọn nhạc. Không cần click chuột để chọn nhạc, chỉ cần để con trỏ vào ô chứa tên nhạc và trỏ ra chỗ khác để nghe thử (khi đã trỏ chuột vào, không được trỏ chuột sang ô khác để tránh bị trỏ nhầm bài, có thể trỏ ra phần không chứa ô nhạc). Vị trí trỏ cuối cùng chính là tên nhạc được chọn. Sau khi nghe và chọn xong nhấn nút Back trên góc để lưu thay đổi nhạc cho game.
- Nút Play: Nhấn vào để chơi với background mặc định của game. Người chơi có thể dùng 2 bên tổ hợp phím để duy chuyển (các nút mũi tên cạnh bàn phím số hoặc các phím A, S, D, W như mấy game khác). Mỗi lần nhặt táo sẽ có điểm boost tốc độ. Nhấn phím cách để sử dụng các điểm đó. Người chơi có tổng cộng 100 mạng để chơi, hứng táo đến khi hết nhạc được chọn sẽ giành chiến thắng, còn không sẽ thua. Sau khi thua có thể nhấn phím Enter để chơi lại hoặc chọn Enter & nút Back để quay lại menu. Nếu thắng thì bấm phím N để chơi lại hoặc chọn Enter & nút Back để quay lại menu.
- Nút Background: Nếu quá chán với background mặc định, có thể chọn 3 background khác để chơi. Chỉ cần click chuột vào 1 trong 3 background để chơi. Cách chơi, luật chơi vẫn giữ nguyên.
