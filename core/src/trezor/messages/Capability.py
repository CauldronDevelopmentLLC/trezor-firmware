# Automatically generated by pb2py
# fmt: off
from trezor import utils

if __debug__:
    try:
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass

Bitcoin: Literal[1] = 1
if not utils.BITCOIN_ONLY:
    Bitcoin_like: Literal[2] = 2
    Binance: Literal[3] = 3
    Cardano: Literal[4] = 4
Crypto: Literal[5] = 5
if not utils.BITCOIN_ONLY:
    EOS: Literal[6] = 6
    Ethereum: Literal[7] = 7
    Lisk: Literal[8] = 8
    Monero: Literal[9] = 9
    NEM: Literal[10] = 10
    Ripple: Literal[11] = 11
    Stellar: Literal[12] = 12
    Tezos: Literal[13] = 13
    U2F: Literal[14] = 14
    Solana: Literal[18] = 18
Shamir: Literal[15] = 15
ShamirGroups: Literal[16] = 16
PassphraseEntry: Literal[17] = 17
