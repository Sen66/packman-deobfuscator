import struct

JMP_patterns = [
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 81 ?? ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 ?? ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? ?? ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 9C 8B ?? 24 81 ?? ?? ?? ?? ?? 89 ?? 24 9D",
    "83 EC ?? 89 ?? 24 9C 8B ?? 24 ?? ?? ?? ?? ?? 89 ?? 24 9D",
    "83 EC ?? 89 ?? 24 9C 8B ?? 24 ?? ?? ?? 89 ?? 24 9D",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 D9 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 DF 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 DA 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 D8 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 DB 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 D9",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 DF",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 DA",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 D8",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 DB",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 81 ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? F7 ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 43 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 42 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 40 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 49 0F ?? ?? ?? ?? ??"
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 4F 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 4B 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 48 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 47 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 41 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 4A 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 43",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 42",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 40",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 49",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 4F",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 4B",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 48",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 47",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 41",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? 4A",    
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? A9 ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 25 ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 3D ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 15 ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 05 ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 0D ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 35 ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 2D ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 ?? ?? ?? ?? ?? A9 ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 25 ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 3D ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 15 ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 05 ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 0D ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 35 ?? ?? ?? ??",
    "83 EC ?? 89 ?? 24 B8 ?? ?? ?? ?? 2D ?? ?? ?? ??",
    "57 BF ?? ?? ?? ?? 81 ?? ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "57 BF ?? ?? ?? ?? F7 ?? ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "57 9C 8B ?? 24 ?? ?? ?? ?? ?? ?? 89 ?? 24 9D",
    "57 BF ?? ?? ?? ?? 47 0F ?? ?? ?? ?? ??",
    "57 BF ?? ?? ?? ?? 4F 0F ?? ?? ?? ?? ??",
    "57 9C 8B ?? 24 ?? ?? ?? 89 ?? 24 9D",
    "57 BF ?? ?? ?? ?? 81 ?? ?? ?? ?? ??",
    "57 BF ?? ?? ?? ?? F7 ?? ?? ?? ?? ??",
    "57 BF ?? ?? ?? ?? 4F",
    "57 BF ?? ?? ?? ?? 47",
    "53 BB ?? ?? ?? ?? 81 ?? ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "53 BB ?? ?? ?? ?? F7 ?? ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "53 9C 8B ?? 24 ?? ?? ?? ?? ?? ?? 89 ?? 24 9D",
    "53 BB ?? ?? ?? ?? 43 0F ?? ?? ?? ?? ??",
    "53 BB ?? ?? ?? ?? 43 0F ?? ?? ?? ?? ??",
    "53 9C 8B ?? 24 ?? ?? ?? 89 ?? 24 9D",
    "53 BB ?? ?? ?? ?? 81 ?? ?? ?? ?? ??",
    "53 BB ?? ?? ?? ?? F7 ?? ?? ?? ?? ??",
    "53 BB ?? ?? ?? ?? 43",
    "53 BB ?? ?? ?? ?? 4B", 
    "52 BA ?? ?? ?? ?? 81 ?? ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "52 BA ?? ?? ?? ?? F7 ?? ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "52 9C 8B ?? 24 ?? ?? ?? ?? ?? ?? 89 ?? 24 9D",
    "52 9C 8B ?? 24 ?? ?? ?? 89 ?? 24 9D",
    "52 BA ?? ?? ?? ?? 4A 0F ?? ?? ?? ?? ??",
    "52 BA ?? ?? ?? ?? 42 0F ?? ?? ?? ?? ??",
    "52 BA ?? ?? ?? ?? 81 ?? ?? ?? ?? ??",
    "52 BA ?? ?? ?? ?? F7 ?? ?? ?? ?? ??",
    "52 BA ?? ?? ?? ?? 4A",
    "52 BA ?? ?? ?? ?? 42", 
    "51 B9 ?? ?? ?? ?? F7 ?? ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "51 B9 ?? ?? ?? ?? 81 ?? ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "51 9C 8B ?? 24 ?? ?? ?? ?? ?? ?? 89 ?? 24 9D",
    "51 B9 ?? ?? ?? ?? 41 0F ?? ?? ?? ?? ??",
    "51 B9 ?? ?? ?? ?? 49 0F ?? ?? ?? ?? ??",
    "51 9C 8B ?? 24 ?? ?? ?? 89 ?? 24 9D",
    "51 B9 ?? ?? ?? ?? F7 ?? ?? ?? ?? ??",
    "51 B9 ?? ?? ?? ?? 81 ?? ?? ?? ?? ??",
    "51 B9 ?? ?? ?? ?? 41",
    "51 B9 ?? ?? ?? ?? 49",
    "50 B8 ?? ?? ?? ?? 35 ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 15 ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 25 ?? ?? ?? ?? 0F ?? ?? ?? ?? ??", 
    "50 B8 ?? ?? ?? ?? 0D ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? A9 ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 3D ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 2D ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 05 ?? ?? ?? ?? 0F ?? ?? ?? ?? ??",
    "50 9C 8B ?? 24 ?? ?? ?? ?? ?? 89 ?? 24 9D",  
    "50 B8 ?? ?? ?? ?? F7 D8 0F ?? ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 40 0F ?? ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 48 0F ?? ?? ?? ?? ??",
    "50 9C 8B ?? 24 ?? ?? ?? 89 ?? 24 9D",          
    "50 B8 ?? ?? ?? ?? 35 ?? ?? ?? ??",  
    "50 B8 ?? ?? ?? ?? 15 ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 25 ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 0D ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? A9 ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 3D ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 2D ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? 05 ?? ?? ?? ??",
    "50 B8 ?? ?? ?? ?? F7 D8",
    "50 B8 ?? ?? ?? ?? 40",
    "50 B8 ?? ?? ?? ?? 48",
]

INDERECT_JMP_patterns = [
    "72 ?? 73 ??",
    "73 ?? 72 ??",
    "70 ?? 71 ??",
    "71 ?? 70 ??",
    "74 ?? 75 ??",
    "75 ?? 74 ??",
    "79 ?? 78 ??",
    "78 ?? 79 ??",
]

LONG_ASS_XOR_patterns = [
  "8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? 8B ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? 31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ??",

  "8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ??",

  "8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ??",

  "8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ??",

  "8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ??",

  "A1 ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? 8B ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ??",

  "A1 ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ??",

  "A1 ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   8B ?? ??",

  "A1 ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ??",

  "A1 ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? \
   8B ??",  

  "A1 ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? \
   31 ?? \
   31 ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ??", 
]

XMM_patterns = [
  "0F ?? ?? ?? ?? ?? ?? \
   85 ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? \
   0F ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? ?? \
   0F ?? ?? \
   0F ?? ?? \
   0F ?? ?? \
   0F ?? ?? \
   0F ?? ?? ?? ?? \
   0F ?? ?? ?? ?? \
   83 ?? ?? \
   39 ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? ??",

  "0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? \
   ?? ?? ?? \
   ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   83 ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? \
   0F ?? ?? ?? ?? \
   0F ?? ?? \
   0F ?? ?? \
   0F ?? ?? \
   0F ?? ?? \
   0F ?? ?? ?? ?? \
   0F ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ??",

  "0F ?? ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? \
   ?? ?? ?? \
   ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   83 ?? ?? \
   ?? ?? \
   66 ?? ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   66 66 ?? ?? ?? ?? 00 00 00 00 00",

  "0F ?? ?? ?? ?? ?? ?? \
   8B ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? \
   ?? ?? ?? \
   ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   83 ?? ?? \
   ?? ?? \
   66 ?? ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ??",

  "A0 ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   89 ?? ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? ?? \
   85 ?? \
   0F ?? ?? ?? ?? ?? \
   33 ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? \
   ?? ?? ?? \
   ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   83 ?? ?? \
   ?? ?? \
   66 ?? ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ??",

  "0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ??",

  "0F ?? ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? ?? \
   85 ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   33 ?? ?? ?? ?? ?? \
   81 ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? \
   83 ?? ?? \
   ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ??",

  "0F ?? ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? ?? \
   85 ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   81 ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? \
   83 ?? ?? \
   ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   83 ?? ?? \
   ?? ?? \
   66 ?? ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ??",

  "0F ?? ?? ?? ?? ?? ?? \
   89 ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   81 ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? \
   ?? ?? ?? \
   ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   83 ?? ?? \
   ?? ?? \
   66 ?? ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   66 66 ?? ?? ?? ?? 00 00 00 00 00",

  "0F ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? ?? \
   85 ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   80 ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   0F ?? ?? \
   ?? \
   ?? ?? ?? \
   ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   83 ?? ?? \
   ?? ?? \
   66 ?? ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ??",

  "0F ?? ?? ?? ?? ?? ?? \
   85 ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   74 ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ??",

  "0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   66 66 66 2E 0F 1F 84 00 00 00 00 00 \
   F3 0F ?? ?? ?? ?? \
   F3 0F ?? ?? ?? ?? \
   F3 0F ?? ?? ?? ?? ?? ?? \
   F3 0F ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   F3 0F ?? ?? ?? ?? \
   F3 0F ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   66 66 66 66 2E 0F 1F 84 00 00 00 00 00",

  "0F ?? ?? ?? ?? ?? ?? \
   89 ?? ?? ?? ?? ?? \
   85 ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   81 ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   66 ?? ?? ?? ?? ?? ?? ?? \
   89 ?? \
   ?? ?? \
   ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   66 66 66 66 66 66 ?? ?? ?? ?? 00 00 00 00 00",

  # UNTESTED, THERE IS inc al; and al 7; instructions sometimes.
  "0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? \
   83 ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   66 ?? ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ??\
   66 0F ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ??",

  "0F ?? ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? ?? \
   89 ?? \
   89 ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? ?? \
   85 ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   81 ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? \
   ?? ?? ?? \
   ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   66 ?? ?? ?? ?? ?? ?? ?? \
   89 ?? \
   ?? ?? \
   ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   66 66 66 66 66 66 ?? ?? ?? ?? 00 00 00 00 00",

  "?? ?? ?? \
   ?? ?? \
   ?? ?? \
   89 ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   81 ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? \
   ?? ?? ?? \
   0F ?? ?? ?? ?? ?? \
   89 ?? \
   89 ?? \
   83 ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   66 ?? ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? ?? \
   ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? ?? \
   83 ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ?? \
   66 66 66 66 66 66 ?? ?? ?? ?? 00 00 00 00 00",

  "0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? \
   3C ?? \
   ?? ?? \
   ?? ?? \
   E9 ?? ?? ?? ?? \
   89 ?? \
   89 ?? \
   ?? ?? ?? \
   ?? ?? \
   ?? ?? ?? ?? ?? \
   ?? ?? \
   66 0F ?? ?? ?? ?? ?? ?? \
   ?? ?? \
   66 0F ?? ?? \
   ?? ?? \
   66 0F ?? ?? \
   ?? ?? ?? \
   0F ?? ?? ?? \
   F3 0F ?? ?? ?? ?? ?? ?? ?? \
   F3 0F ?? ?? ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   ?? ?? \
   66 0F ?? ?? \
   ?? ?? \
   ?? ?? \
   66 0F ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? ?? \
   66 0F ?? ?? \
   66 0F ?? ?? \
   ?? ?? \
   0F ?? ?? ?? ?? ?? ??"
    
  # "89 ?? \
  #  89 ?? \
  #  83 ?? ?? \
  #  83 ?? ?? \
  #  ?? ?? \
  #  66 ?? ?? ?? ?? ?? ?? ?? \
  #  ?? ?? \
  #  ?? ?? \
  #  ?? ?? ?? \
  #  66 0F ?? ?? ?? ?? ?? ?? ?? \
  #  66 0F ?? ?? ?? ?? ?? ?? ?? \
  #  66 0F ?? ?? ?? ?? \
  #  66 0F ?? ?? ?? ?? \
  #  66 0F ?? ?? \
  #  66 0F ?? ?? \
  #  66 0F ?? ?? \
  #  66 0F ?? ?? \
  #  66 0F ?? ?? ?? ?? \
  #  66 0F ?? ?? ?? ?? \
  #  83 ?? ?? \
  #  ?? ?? \
  #  ?? ?? \
  #  ?? ?? \
  #  ?? ??",

  # "89 ?? \
  #  89 ?? \
  #  ?? ?? ?? \
  #  ?? ?? \
  #  ?? ?? \
  #  66 0F ?? ?? ?? ?? ?? ?? \
  #  89 ?? \
  #  66 0F ?? ?? \
  #  ?? ?? ??  \
  #  ?? ?? ?? ?? \
  #  ?? ?? \
  #  ?? ?? ?? \
  #  ?? ?? \
  #  F3 0F ?? ?? ?? \
  #  F3 0F ?? ?? \
  #  ?? ?? ?? \
  #  ?? ?? ?? \
  #  66 0F ?? ?? \
  #  66 0F ?? ?? \
  #  66 0F ?? ?? \
  #  66 0F ?? ?? \
  #  ?? ?? \
  #  66 0F ?? ?? \
  #  ?? ?? \
  #  66 0F ?? ?? ?? \
  #  66 0F ?? ?? \
  #  66 0F ?? ?? ?? \
  #  66 0F ?? ?? \
  #  66 0F ?? ?? \
  #  ?? ?? \
  #  ?? ??",
]

lol = [
  "?? ?? ?? \
   BA ?? ?? ?? ?? \
   69 ?? ?? ?? ?? ?? \
   0F ?? ?? \
   31 ?? \
   ?? ?? \
   C1 ?? ?? \
   F7 ?? \
   01 ?? \
   01 ?? \
   0F ?? ?? \
   83 ?? ?? \
   ?? ?? ?? \
   ?? ?? \
   EB ??",

  "89 ?? \
   ?? ?? \
   ?? ?? \
   81 ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   F7 ?? \
   0F ?? ?? ?? ?? ?? ?? ?? \
   30 ?? ?? ?? ?? ?? \
   ?? \
   A1 ?? ?? ?? ?? \
   ?? ?? \
   ?? ?? \
   ?? ??"
]

kek = [
  "0F ?? ?? ?? ?? ?? ?? \
   32 ?? ?? ?? \
   ?? ?? ?? \
   88 ?? ?? ?? \
   ?? \
   ?? ?? ?? \
   ?? ??",
  
  "8B ?? ?? ?? \
   33 ?? ?? ?? ?? ?? ?? \
   81 ?? ?? ?? ?? ?? \
   ?? ?? ?? ?? \
   ?? \
   39 ?? \
   ?? ??",

  "8B ?? ?? \
   33 ?? ?? ?? ?? ?? ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? \
   ?? \
   39 ?? \
   ?? ??",

  "0F ?? ?? ?? ?? ?? ?? \
   ?? ?? ?? \
   80 ?? ?? \
   88 ?? ?? \
   ?? \
   83 ?? ?? \
   ?? ??",

  "0F ?? ?? ?? ?? ?? ?? \
   32 ?? ?? \
   ?? ?? \
   88 ?? ?? \
   ?? \
   83 ?? ??\
   ?? ??",
  
  "0F ?? ?? ?? ?? ?? ?? \
   32 ?? ?? ?? \
   34 ?? \
   88 ?? ?? ?? \
   ?? \
   83 ?? ?? \
   ?? ??",

  "8B ?? ?? \
   33 ?? ?? ?? ?? ?? ?? \
   35 ?? ?? ?? ?? \
   ?? ?? ?? \
   ?? \
   39 ?? \
   ?? ??",

  "33 ?? \
   83 ?? ?? \
   81 ?? ?? ?? ?? ?? \
   ?? \
   75 ??",

  "33 ?? \
   83 ?? ?? \
   35 ?? ?? ?? ?? \
   49 \
   75 ??",
  
  "8B ?? ?? ?? ?? ?? ?? \
   33 ?? ?? ?? ?? ?? ?? \
   81 ?? ?? ?? ?? ?? \
   89 ?? ?? ?? ?? ?? ?? \
   ?? \
   39 ?? \
   ?? ??",
  
  "0F ?? ?? ?? ?? ?? ?? \
   32 ?? ?? ?? ?? ?? ?? \
   80 ?? ?? \
   88 ?? ?? ?? ?? ?? ?? \
   ?? \
   83 ?? ?? \
   ?? ??",

  "8A ?? ?? ?? ?? ?? \
   32 ?? ?? ?? ?? ?? ?? \
   80 ?? ?? \
   88 ?? ?? ?? ?? ?? ?? \
   ?? \
   83 ?? ?? \
   75 ??",
   
  "33 ?? ?? ?? ?? ?? ?? \
   ?? \
   81 ?? ?? ?? ?? ?? \
   39 ?? \
   75 ??"
]
class Template:
  def __init__(self):
    pass

  def find_all(self, start, end, seq):
    res = list()
    addr = find_binary(start, SEARCH_DOWN | SEARCH_NEXT, seq)
    while (addr <= end and addr != BADADDR):
      res.append(addr)
      addr = find_binary(addr, SEARCH_DOWN | SEARCH_NEXT, seq)
    return res

  def patch(self, dest, seq):
    for i, c in enumerate(seq):
      idc.PatchByte(dest+i, ord(c))

  def disasm(self, dest, length):
    dis = list()
    end = dest + length
    while (dest <= end):
      dis.append(dest)
      dest = next_head(dest, end)
    return dis

  def hide(self, addr, length):
    HideArea(addr, addr+length, "", "", "", 0xEEFFFFFF)

  def toCode(self, addr, length):
    for i in range(length):
      MakeCode(addr + i)

class lol(Template):

  def __init__(self):
    self.start = get_segm_by_sel(0)                    # only for .text section
    self.end = get_segm_end(self.start)
    self.count = 0

  def patch_jmps(self, seq):
    seq_len, sz = len(seq.split()), 0
    addrs = self.find_all(self.start, self.end, seq)
    for addr in addrs:
      jmp_offset = Byte(addr + seq_len + 1)               # get short jump offset
      self.patch(addr, "\x90" * seq_len + "\xEB")         # nop junk instructions
      self.hide(addr + seq_len + 2, jmp_offset)           # hide junk data
      length = seq_len + 2 + jmp_offset                   # get total junk length
      MakeCode(addr + length)
      opcode = print_insn_mnem(addr + length)             # calc how much code you have to nop
      if opcode == "pop":
        sz = 1
        MakeCode(addr + length + 1)
        if print_insn_mnem(addr + length + 1) == "add":
          sz = 4
      elif opcode == "mov":
        sz = 6
      
      self.patch(addr + length, "\x90" * sz)
      self.count += 1

  def patch_inderect_jmps(self, seq):
    addrs = self.find_all(self.start, self.end, seq)
    for addr in addrs:
      
      if Byte(addr+1) == Byte(addr + 3) + 2:              # check if both jmps to the same loc
        jmp_offset = Byte(addr + 1)                       # get jmp offset
        self.patch(addr, "\xEB")                        # insert DIRECT jmp 
        self.hide(addr + 2, jmp_offset)                 # hide junk data
        self.count += 1

  def patch_mov_xors(self, seq):

    regs = {
      "eax" : "\xB8",
      "ecx" : "\xB9",
      "edx" : "\xBA",
      "ebx" : "\xBB", 
      "esp" : "\xBC",
      "ebp" : "\xBD",   
      "esi" : "\xBE",
      "edi" : "\xBF",
    }

    seq_len = len(seq.split())
    addrs = self.find_all(self.start, self.end, seq)
    for addr in addrs:
      for i in range(seq_len):
        MakeCode(addr + i)
      heads = self.disasm(addr, seq_len)
      if len(heads) <= 14:
        if GetOperandValue(heads[0], 1) != GetOperandValue(heads[1], 1):
          continue
        if GetOperandValue(heads[6], 1) != GetOperandValue(heads[7], 1):
          continue

        answer = GetOperandValue(heads[3], 1) ^ GetOperandValue(heads[10], 1)
        operand = print_operand(heads[12], 0)

      else:
        if seq_len != 107:
          if GetOperandValue(heads[0], 1) != GetOperandValue(heads[1], 1):
            continue
          if GetOperandValue(heads[6], 1) != GetOperandValue(heads[7], 1):
            continue
          if GetOperandValue(heads[13], 1) != GetOperandValue(heads[14], 1):
            continue
          if GetOperandValue(heads[20], 1) != GetOperandValue(heads[21], 1):
            continue

          answer = GetOperandValue(heads[3], 1) ^ GetOperandValue(heads[10], 1) ^ \
            GetOperandValue(heads[17], 1) ^ GetOperandValue(heads[24], 1)
          operand = print_operand(heads[26], 0)

        else:
          if GetOperandValue(heads[0], 1) != GetOperandValue(heads[1], 1):
            continue
          if GetOperandValue(heads[6], 1) != GetOperandValue(heads[7], 1):
            continue
          if GetOperandValue(heads[13], 1) != GetOperandValue(heads[14], 1):
            continue
          if GetOperandValue(heads[19], 1) != GetOperandValue(heads[20], 1):
            continue

          answer = GetOperandValue(heads[3], 1) ^ GetOperandValue(heads[10], 1) ^ \
            GetOperandValue(heads[16], 1) ^ GetOperandValue(heads[23], 1)
          operand = print_operand(heads[25], 0)

      self.patch(addr, "\x90" * (seq_len - 5) + regs[operand] + struct.pack("<I", answer))
      for i in range(seq_len):
        MakeCode(addr + i)
      self.count += 1

  def patch_xmm(self, seq):
    seq_len = len(seq.split())
    addrs = self.find_all(self.start, self.end, seq)
    print addrs
    for addr in addrs:
      self.toCode(addr - 0x30, seq_len + 0x30)
      self.patch(addr, "\x90" * seq_len)
      heads = self.disasm(addr, seq_len)
      print print_insn_mnem(heads[-2]), print_insn_mnem(heads[-1])
      # sz_before = heads[-2] - addr
      # self.patch(addr, "\x90" * sz_before)
      # self.patch(addr + sz_before, "\xEB")
      self.count += 1
      

  def run(self):
    for pattern in JMP_patterns:
      self.patch_jmps(pattern)

    for pattern in INDERECT_JMP_patterns:
      self.patch_inderect_jmps(pattern)

    for pattern in LONG_ASS_XOR_patterns:
      self.patch_mov_xors(pattern)

    for pattern in kek:
      self.patch_xmm(pattern)

    for pattern in XMM_patterns:
      self.patch_xmm(pattern)

    print "patched %d places" % self.count
    self.count = 0
# 
# 6B2A5230 - unhandled 100B795A
x = lol()
x.run()

# 66 66 66 66 66 66 2E 0F 1F 84 00 00 00 00 00 NOP
"""[268873491L, 268874848L, 270540661L, 270544421L, 270593373L, 270594102L, 270599453L, 270600399L, 270605578L, 270606286L, 270611697L, 270612643L, 270617816L, 270618552L, 270623963L, 270624909L, 270630098L, 270630813L, 270636245L, 270637191L, 270642370L, 270643119L, 270648572L, 270649518L, 270654692L, 270655403L, 270660851L, 270661797L, 270666987L, 270667718L, 270673166L, 270674112L, 270679284L, 270679991L, 270685435L, 270686381L, 270691549L, 270692278L, 270697717L, 270698663L, 270703837L, 270704559L, 270710003L, 270710949L, 270716132L, 270716862L, 270722297L, 270723031L, 270724971L, 270725917L, 270731110L, 270731824L, 270737268L, 270738214L, 270743379L, 270744091L, 270749574L, 270750520L, 270755687L, 270756416L, 270761860L, 270762806L, 270767998L, 270768736L, 270774180L, 270775014L, 270780150L, 270780720L, 270786164L, 270786998L, 270792069L, 270792637L, 270802461L, 270803295L, 270810494L, 270811078L, 270814429L, 270815264L, 270822404L, 270822982L, 270826332L, 270827167L, 270835692L, 270836269L, 270838241L, 270839076L, 270847601L, 270848176L, 270850148L, 270850983L, 270859493L, 270860049L, 270862021L, 270862856L, 270871374L, 270871926L, 270873898L, 270874733L, 270883260L, 270883826L, 270885798L, 270886633L, 270895161L, 270895740L, 270897712L, 270898547L, 270907053L, 270907614L, 270909586L, 270910421L, 270918965L, 270920643L]"""