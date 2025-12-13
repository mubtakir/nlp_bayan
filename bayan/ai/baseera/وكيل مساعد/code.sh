sudo apt-get update
sudo apt-get install python3.9 python3-pip -y # أو أحدث إصدار python3 متوافق
# انتقل إلى مجلد المشروع إذا لم تكن فيه
# cd path/to/your/project_root # المجلد الذي يحتوي على my_mcp_agent
# pip install -r my_mcp_agent/requirements.txt # إذا كنت قد أعددت ملف requirements.txt مسبقًا
# أو قم بتثبيت المكتبات بشكل فردي:
pip install python-dotenv requests openai flask # langchain اختيارية إذا لم تكن تستخدمها بشكل مكثف