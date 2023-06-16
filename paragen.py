#author: Kshitij
#github: https://github.com/krrysis
#email: kshitijshukla345@gmail.com


ip=input("Enter IP: ")
def search_sentences(sentences, words):
    paragraph = "Please find the vulnerability scan results for 192.168." + ip +" below: \n"
    for sentence in sentences:
        for word in words:
            if word.lower() in sentence.lower():
                paragraph += " "
                paragraph +=" "+ sentence + " "
                break
    return paragraph.strip().replace("@","\n")
    

sentences =      ["@• WinVerifyTrust Signature Validation CVE-2013-3900 Mitigation: Apply registry keys from the following path: \n \\192.168.109.200\MOTCommon\Infosec\VA\winverifyRegistryKeys \n Apply both enableAuthenticodeVerification.reg and enableAuthenticodeVerification64.reg@",
                  "@• Information Disclosure vulnerability: Apply both registry keys from the following path: \n \\192.168.109.200\MOTCommon\Infosec\VA\2016IDVkeys@",
                  "@• Terminal Services Doesn't Use Network Level Authentication (NLA) Only \n Solution \n Enable Network Level Authentication (NLA) on the remote RDP server. @",
                  "@• SMB Signing not required. Enforce message signing in the host's configuration. On Windows, this is found in the policy setting 'Microsoft network server: Digitally sign communications (always)'.@",
                  "@• Curl Use-After-Free < 7.87. Installed version: 7.83.1.0  Fixed version: 7.87.0@",
                  "@• SSL Medium Strength Cipher Suites Supported (SWEET32). Reconfigure to avoid use of DES/3DES ciphers.@",
                  "@• Disable TLS 1.0@",
                  "@• Disable TLS 1.1@"
                  ]


words = input("Enter comma-separated words: ").split(",")
print(search_sentences(sentences, words))
