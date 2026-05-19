default:
    just -l

gds:
    python3.11 art/make_gds.py -i art/miku-juno.png -c art -o art/art.gds -v

harden:
    python3.11 tt/tt_tool.py --harden

config:
    python3.11 tt/tt_tool.py --create-user-config