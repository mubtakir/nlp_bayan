from bayan.bayan import HybridLexer, HybridParser, HybridInterpreter


def run_interp(code: str) -> HybridInterpreter:
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    program = parser.parse()
    interp = HybridInterpreter()
    interp.interpret(program)
    return interp


def test_data_scalers_wave8():
    code = """
    from ai.data import standard_scaler_fit, standard_scaler_transform
    from ai.data import robust_scaler_fit, robust_scaler_transform
    from ai.data import minmax_scaler_fit, minmax_scaler_transform
    hybrid {
      xs = [1.0, 2.0, 3.0]
      # standard
      ms = standard_scaler_fit(xs)
      xz = standard_scaler_transform(xs, ms[0], ms[1])
      m = ms[0]
      s = ms[1]
      # robust
      mr = robust_scaler_fit(xs)
      xr = robust_scaler_transform(xs, mr[0], mr[1])
      # minmax
      mm = minmax_scaler_fit(xs)
      xm = minmax_scaler_transform(xs, mm[0], mm[1])
    }
    """
    interp = run_interp(code)
    env = interp.traditional.global_env
    m = env.get('m'); s = env.get('s')
    xz = env.get('xz'); xr = env.get('xr'); xm = env.get('xm')
    # mean ~ 2.0 and std ~ 0.81649658 for population std of [1,2,3]
    assert abs(m - 2.0) < 1e-6
    assert abs(s - (2.0/3.0)**0.5) < 1e-6
    # standardized values ~ [-1.2247, 0.0, 1.2247]
    assert len(xz) == 3
    assert abs(xz[0] + 1.224744871) < 1e-3
    assert abs(xz[1] - 0.0) < 1e-6
    assert abs(xz[2] - 1.224744871) < 1e-3
    # robust: median=2, IQR=2 -> [-0.5,0,0.5]
    assert xr == [-0.5, 0.0, 0.5]
    # minmax: [0,0.5,1]
    assert xm == [0.0, 0.5, 1.0]

