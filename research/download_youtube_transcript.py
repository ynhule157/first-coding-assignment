import subprocess
from pathlib import Path

VIDEO_ID = "A30GKOnOSrI"
OUT_DIR = Path("research/youtube-transcripts")

def main():
    # Tạo sẵn ngăn chứa trong nhà kho
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{VIDEO_ID}.md"

    try:
        # Tuyệt chiêu: Ép hệ thống tự chạy ngầm để lấy dữ liệu
        print("Đang lấy dữ liệu ngầm, Alex đợi 2 giây nha...")
        result = subprocess.run(
            ["python", "-m", "youtube_transcript_api", VIDEO_ID],
            capture_output=True, text=True, check=True
        )
        
        # Đóng gói dữ liệu vào file
        md_content = f"# Transcript for Video ID: {VIDEO_ID}\n\n## Data\n\n```text\n{result.stdout}\n```"
        out_path.write_text(md_content, encoding="utf-8")
        
        print(f"\nXUẤT SẮC! Đã lưu thành công tại: {out_path.resolve()}\n")
        
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()