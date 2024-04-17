figlet SETUP . sh | lolcat
arch_yay() {
    if ! which yay > /dev/null; then
    clear
    sudo pacman -Syu --noconfirm
    sudo pacman -S --needed base-devel git --noconfirm
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si  --noconfirm
fi
}
sudo pacman -S python-pip --noconfirm
sudo pacman -S --noconfirm tk python-pillow
pip3 install pillow --break-system-packages
arch_yay

clear
echo " Run as: python3 Nvidiainstaller.py" | lolcat
echo
