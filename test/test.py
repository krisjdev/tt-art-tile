# SPDX-FileCopyrightText: © 2026 Kristaps Jurkans
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    assert True
