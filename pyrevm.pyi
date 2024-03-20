from typing import Optional, Type, Tuple


class CfgEnv:
    def __new__(cls: Type["CfgEnv"]) -> "CfgEnv": ...

class BlockEnv:
    def __new__(
        cls: Type["BlockEnv"],
        number: Optional[int] = None,
        coinbase: Optional[str] = None,
        timestamp: Optional[int] = None,
        difficulty: Optional[int] = None,
        prevrandao: Optional[bytes] = None,
        basefee: Optional[int] = None,
        gas_limit: Optional[int] = None,
    ) -> "BlockEnv": ...

    @property
    def number(self) -> Optional[int]: ...
    @property
    def coinbase(self) -> Optional[str]: ...
    @property
    def timestamp(self) -> Optional[int]: ...
    @property
    def difficulty(self) -> Optional[int]: ...
    @property
    def prevrandao(self) -> Optional[bytes]: ...
    @property
    def basefee(self) -> Optional[int]: ...
    @property
    def gas_limit(self) -> Optional[int]: ...

class TxEnv:
    def __new__(
        cls: Type["TxEnv"],
        caller: Optional[str] = None,
        gas_limit: Optional[int] = None,
        gas_price: Optional[int] = None,
        gas_priority_fee: Optional[int] = None,
        to: Optional[str] = None,
        value: Optional[int] = None,
        data: Optional[bytes] = None,
        chain_id: Optional[int] = None,
        nonce: Optional[int] = None,
    ) -> "TxEnv": ...

    @property
    def caller(self) -> Optional[str]: ...
    @property
    def gas_limit(self) -> Optional[int]: ...
    @property
    def gas_price(self) -> Optional[int]: ...
    @property
    def gas_priority_fee(self) -> Optional[int]: ...
    @property
    def to(self) -> Optional[str]: ...
    @property
    def value(self) -> Optional[int]: ...
    @property
    def data(self) -> Optional[bytes]: ...
    @property
    def chain_id(self) -> Optional[int]: ...
    @property
    def nonce(self) -> Optional[int]: ...

class Env:
    def __new__(
        cls: Type["Env"],
        cfg: Optional[CfgEnv] = None,
        block: Optional[BlockEnv] = None,
        tx: Optional[TxEnv] = None,
    ) -> "Env": ...
    @property
    def cfg(self: "AccountInfo") -> Optional[CfgEnv]: ...
    @property
    def block(self: "AccountInfo") -> Optional[BlockEnv]: ...
    @property
    def tx(self: "AccountInfo") -> Optional[TxEnv]: ...


class JournalCheckpoint:
    @property
    def log_i(self) -> int: ...
    @property
    def journal_i(self) -> int: ...


class AccountInfo:
    def __new__(
        cls: Type["AccountInfo"],
        nonce: int = 0,
        code_hash: Optional[bytes] = None,
        code: Optional[bytes] = None,
    ) -> "AccountInfo": ...

    @property
    def balance(self: "AccountInfo") -> int: ...
    @property
    def nonce(self: "AccountInfo") -> int: ...
    @property
    def code(self: "AccountInfo") -> bytes: ...
    @property
    def code_hash(self: "AccountInfo") -> bytes: ...

class EVM:
    def __new__(
        cls: Type["EVM"],
        env: Optional[Env] = None,
        fork_url: Optional[str] = None,
        fork_block_number: Optional[str] = None,
        gas_limit: int = 2**64 - 1,
        tracing: bool = False,
        spec_id="SHANGHAI",
    ) -> "EVM":
        """
        Creates a new EVM instance.
        :param env: The environment.
        :param gas_limit: The gas limit.
        :param tracing: Whether to enable tracing.
        :param spec_id: The spec ID.
        """

    def snapshot(self: "EVM") -> JournalCheckpoint: ...

    def revert(self: "EVM", checkpoint: JournalCheckpoint) -> None: ...
    def commit(self: "EVM") -> None: ...

    def basic(self: "EVM", address: str) -> AccountInfo:
        """
        Returns the basic account info for the given address.
        :param address: The address of the account.
        :return: The account info.
        """

    def insert_account_info(self: "EVM", address: str, info: AccountInfo) -> None:
        """
        Inserts the given account info into the state.
        :param address: The address of the account.
        :param info: The account info.
        """

    def call_raw_committing(
        self: "EVM",
        caller: str,
        to: str,
        calldata: Optional[bytes] = None,
        value: Optional[int] = None,
    ) -> bytes:
        """
        Processes a raw call, committing the result to the state.
        :param caller: The address of the caller.
        :param to: The address of the callee.
        :param calldata: The data to pass to the contract.
        :param value: The value.
        :return: The return data.
        """

    def call_raw(
        self: "EVM",
        caller: str,
        to: str,
        calldata: Optional[bytes] = None,
        value: Optional[int] = None,
    ) -> Tuple[bytes, dict[str, AccountInfo]]:
        """
        Processes a raw call, without committing the result to the state.
        :param caller: The address of the caller.
        :param to: The address of the callee.
        :param calldata: The calldata.
        :param value: The value.
        :return: The return data and a list of changes to the state.
        """

    def deploy(
        self: "EVM",
        deployer: str,
        code: bytes,
        value: Optional[int] = None,
    ) -> str:
        """
        Deploys the given code.
        :param deployer: The address of the deployer.
        :param code: The code.
        :param value: The value.
        :return: The address of the deployed contract.
        """

    def get_balance(self: "EVM", address: str) -> int:
        """
        Returns the balance of the given address.
        :param address: The address.
        :return: The balance.
        """

    def set_balance(self: "EVM", address: str, balance: int) -> None:
        """
        Sets the balance of the given address.
        :param address: The address.
        :param balance: The balance.
        """

    def storage(self: "EVM", address: str, index: int) -> int:
        """
        Returns the storage value of the given address at the given index.
        :param address: The address.
        :param index: The index.
        :return: The storage value.
        """

    @property
    def env(self: "EVM") -> Env:
        """ Get the environment. """

    @property
    def tracing(self: "EVM") -> bool:
        """ Whether tracing is enabled. """
