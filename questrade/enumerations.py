"""
Usage:  Questrade API Enumerations
File:   enumerations.py
Created by T.Wang at 20.Nov.2023
"""


# The following table specifies all supported currency codes.
class Currency:
    USD = 'USD'
    CAD = 'CAD'


# The following table specifies all supported listing exchanges.
class ListingExchange:
    TSX = "TSX"  # Toronto Stock Exchange.
    TSXV = "TSXV"  # Toronto Venture Exchange.
    CNSX = "CNSX"  # Canadian National Stock Exchange.
    MX = "MX"  # Montreal Exchange.
    NASDAQ = "NASDAQ"  # NASDAQ.
    NYSE = "NYSE"  # New York Stock Exchange.
    NYSEAM = "NYSEAM"  # NYSE AMERICAN
    ARCA = "ARCA"  # NYSE Arca.
    OPRA = "OPRA"  # Option Reporting Authority.
    PinkSheets = "PinkSheets"  # Pink Sheets.
    OTCBB = "OTCBB"  # OTC Bulletin Board.


# The following table specifies all supported user account types.
class AccountType:
    CASH = "Cash"  # Cash account.
    MARGIN = "Margin"  # Margin account.
    TFSA = "TFSA"  # Tax Free Savings Account.
    RRSP = "RRSP"  # Registered Retirement Savings Plan.
    FHSA = "FHSA"  # First Home Savings Account.
    SRRSP = "SRRSP"  # Spousal RRSP.
    LRRSP = "LRRSP"  # Locked-In RRSP.
    LIRA = "LIRA"  # Locked-In Retirement Account.
    LIF = "LIF"  # Life Income Fund.
    RIF = "RIF"  # Retirement Income Fund.
    SRIF = "SRIF"  # Spousal RIF.
    LRIF = "LRIF"  # Locked-In RIF.
    RRIF = "RRIF"  # Registered RIF.
    PRIF = "PRIF"  # Prescribed RIF.
    RESP = "RESP"  # Individual Registered Education Savings Plan.
    FRESP = "FRESP"  # Family RESP.


# The following table specifies all supported account client types.
class ClientAccountType:
    INDIVIDUAL = "Individual"  # Account held by an individual.
    JOINT = "Joint"  # Account held jointly by several individuals (e.g., spouses).
    INFORMAL_TRUST = "Informal Trust"  # Non-individual account held by an informal trust.
    CORPORATION = "Corporation"  # Non-individual account held by a corporation.
    INVESTMENT_CLUB = "Investment Club"  # Non-individual account held by an investment club.
    FORMAL_TRUST = "Formal Trust"  # Non-individual account held by a formal trust.
    PARTNERSHIP = "Partnership"  # Non-individual account held by a partnership.
    SOLE_PROPRIETORSHIP = "Sole Proprietorship"  # Non-individual account held by a sole proprietorship.
    FAMILY = "Family"  # Account held by a family.
    JOINT_AND_INFORMAL_TRUST = "Joint and Informal Trust"  # Non-individual account held by a joint and informal trust.
    INSTITUTION = "Institution"  # Non-individual account held by an institution.


# The following table specifies all supported account status values.
class AccountStatus:
    ACTIVE = "Active"  #
    SUSPENDED_CLOSED = "Suspended (Closed)"  #
    SUSPENDED_VIEW_ONLY = "Suspended (View Only)"  #
    LIQUIDATE_ONLY = "Liquidate Only"  #
    CLOSED = "Closed"  #


# The following table specifies all supported market data tick types.
class TickType:
    UP = "Up"  # Designates an uptick.
    DOWN = "Down"  # Designates a downtick.
    EQUAL = "Equal"  # Designates a tick that took place at the same price as a previous one.


# The following table specifies all supported option types.
class OptionType:
    CALL = "Call"  # Call option.
    PUT = "Put"  # Put option.


# The following table specifies all supported option duration types.
class OptionDurationType:
    WEEKLY = "Weekly"  # Weekly expiry cycle.
    MONTHLY = "Monthly"  # Monthly expiry cycle.
    QUARTERLY = "Quarterly"  # Quarterly expiry cycle.
    LEAP = "LEAP"  # Long-term Equity Appreciation contracts.


# The following table specifies all supported option exercise types.
class OptionExciseType:
    AMERICAN = "American"  # American option.
    EUROPEAN = "European"  # European option.


# The following table specifies all supported security types.
class SecurityType:
    STOCK = "Stock"  # Common and preferred equities, ETFs, ETNs, units, ADRs, etc.
    OPTION = "Option"  # Equity and index options.
    BOND = "Bond"  # Debentures, notes, bonds, both corporate and government.
    RIGHT = "Right"  # Equity or bond rights and warrants.
    GOLD = "Gold"  # Physical gold (coins, wafers, bars).
    MUTUAL_FUND = "MutualFund"  # Canadian or US mutual funds.
    INDEX = "Index"  # Stock indices (e.g., Dow Jones).


# The following table specifies all supported order state filter types.
class OrderStateFilterType:
    ALL = "All"  # Includes all orders, regardless of their state.
    OPEN = "Open"  # Includes only orders that are still open.
    CLOSED = "Closed"  # Includes only orders that are already closed.


# The following table specifies all supported order side values.
class OderAction:
    BUY = "Buy"  # Designates an order to purchase a security.
    SELL = "Sell"  # Designates an order to dispose a security.


# The following table specifies all supported client order side values.
class OderSide:
    BUY = "Buy"  # Buy
    SELL = "Sell"  # Sell
    SHORT = "Short"  # Sell short.
    COV = "Cov"  # Cover the short.
    BTO = "BTO"  # Buy-To-Open.
    STC = "STC"  # Sell-To-Close.
    STO = "STO"  # Sell-To-Open.
    BTC = "BTC"  # Buy-To-Close.


# The following table specifies all supported order types.
class OderType:
    MARKET = "Market"  #
    LIMIT = "Limit"  #
    STOP = "Stop"  #
    STOP_LIMIT = "StopLimit"  #
    TRAIL_STOP_IN_PERCENTAGE = "TrailStopInPercentage"  #
    TRAIL_STOP_IN_DOLLAR = "TrailStopInDollar"  #
    TRAIL_STOP_LIMIT_IN_PERCENTAGE = "TrailStopLimitInPercentage"  #
    TRAIL_STOP_LIMIT_IN_DOLLAR = "TrailStopLimitInDollar"  #
    LIMIT_ON_OPEN = "LimitOnOpen"  #
    LIMIT_ON_CLOSE = "LimitOnClose"  #


# The following table specifies all supported order Time-In-Force instructions.
class OrderTimeInForce:
    DAY = "Day"  #
    GOOD_TILL_CANCELED = "GoodTillCanceled"  #
    GOOD_TILL_EXTENDED_DAY = "GoodTillExtendedDay"  #
    GOOD_TILL_DATE = "GoodTillDate"  #
    IMMEDIATE_OR_CANCEL = "ImmediateOrCancel"  #
    FILL_OR_KILL = "FillOrKill"  #


# The following table specifies all supported order states.
class OderState:
    FAILED = "Failed"  #
    PENDING = "Pending"  #
    ACCEPTED = "Accepted"  #
    REJECTED = "Rejected"  #
    CANCEL_PENDING = "CancelPending"  #
    CANCELED = "Canceled"  #
    PARTIAL_CANCELED = "PartialCanceled"  #
    PARTIAL = "Partial"  #
    EXECUTED = "Executed"  #
    REPLACE_PENDING = "ReplacePending"  #
    REPLACED = "Replaced"  #
    STOPPED_ = "Stopped"  #
    SUSPENDED = "Suspended"  #
    EXPIRED_ = "Expired"  #
    QUEUED_ = "Queued"  #
    TRIGGERED = "Triggered"  #
    ACTIVATED = "Activated"  #
    PENDING_RISK_REVIEW = "PendingRiskReview"  #
    CONTINGENT_ORDER = "ContingentOrder"  #


# The following table specifies all supported order execution status values.
class HistoricalDataGranularity:
    ONE_MINUTE = "OneMinute"  # One candlestick per 1 minute.
    TWO_MINUTES = "TwoMinutes"  # One candlestick per 2 minutes.
    THREE_MINUTES = "ThreeMinutes"  # One candlestick per 3 minutes.
    FOUR_MINUTES = "FourMinutes"  # One candlestick per 4 minutes.
    FIVE_MINUTES = "FiveMinutes"  # One candlestick per 5 minutes.
    TEN_MINUTES = "TenMinutes"  # One candlestick per 10 minutes.
    FIFTEEN_MINUTES = "FifteenMinutes"  # One candlestick per 15 minutes.
    TWENTY_MINUTES = "TwentyMinutes"  # One candlestick per 20 minutes.
    HALF_HOUR = "HalfHour"  # One candlestick per 30 minutes.
    ONE_HOUR = "OneHour"  # One candlestick per 1 hour.
    TWO_HOURS = "TwoHours"  # One candlestick per 2 hours.
    FOUR_HOURS = "FourHours"  # One candlestick per 4 hours.
    ONE_DAY = "OneDay"  # One candlestick per 1 day.
    ONE_WEEK = "OneWeek"  # One candlestick per 1 week.
    ONE_MONTH = "OneMonth"  # One candlestick per 1 month.
    ONE_YEAR = "OneYear"  # One candlestick per 1 year.


# The following table specifies all supported bracket order components.
class OderClas:
    PRIMARY = "Primary"  # Primary order
    LIMIT = "Limit"  # Profit exit order
    STOP_LOSS = "StopLoss"  # Loss exit order


# The following types of strategies are supported for multi-leg strategy orders
class StrategyTypes:
    COVERED_CALL = "CoveredCall"  # Covered Call
    MARRIED_PUTS = "MarriedPuts"  # Married Put
    VERTICAL_CALL_SPREAD = "VerticalCallSpread"  # Vertical Call
    VERTICAL_PUT_SPREAD = "VerticalPutSpread"  # Vertical Put
    CALENDAR_CALL_SPREAD = "CalendarCallSpread"  # Calendar Call
    CALENDAR_PUT_SPREAD = "CalendarPutSpread"  # Calendar Put
    DIAGONAL_CALL_SPREAD = "DiagonalCallSpread"  # Diagonal Call
    DIAGONAL_PUT_SPREAD = "DiagonalPutSpread"  # Diagonal Put
    COLLAR = "Collar"  # Collar
    STRADDLE = "Straddle"  # Straddle
    STRANGLE = "Strangle"  # Strangle
    BUTTERFLY_CALL = "ButterflyCall"  # Butterfly Call
    BUTTERFLY_PUT = "ButterflyPut"  # Butterfly Put
    IRON_BUTTERFLY = "IronButterfly"  # Iron Butterfly
    CONDOR_CALL = "CondorCall"  # Condor
    CUSTOM = "Custom"  # Custom, or user defined
