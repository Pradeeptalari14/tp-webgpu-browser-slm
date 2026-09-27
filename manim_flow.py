from manim import *

class WebGPUBrowserSLMScene(Scene):
    def construct(self):
        title = Text("WebGPU: Zero-Server In-Browser SLM Inference", font_size=32, color=TEAL).to_edge(UP)
        self.play(Write(title))

        browser_box = Rectangle(height=3.0, width=4.5, color=CYAN, fill_opacity=0.3).shift(LEFT * 3)
        b_label = Text("Browser Sandbox\n(WebGPU WGSL GEMM)", font_size=18, color=WHITE).move_to(browser_box.get_top() + DOWN * 0.4)
        vram_box = Rectangle(height=1.2, width=3.8, color=GREEN, fill_opacity=0.6).move_to(browser_box.get_bottom() + UP * 0.8)
        vram_lbl = Text("Local GPU VRAM\n(SmolLM2 142MB)", font_size=16).move_to(vram_box)
        self.play(Create(browser_box), Write(b_label), Create(vram_box), Write(vram_lbl))

        server_box = Rectangle(height=3.0, width=4.0, color=RED, fill_opacity=0.2).shift(RIGHT * 3.5)
        cross = Cross(server_box, color=RED)
        s_label = Text("External Server / Cloud\n(0 Network Calls)", font_size=18, color=RED_A).move_to(server_box)
        self.play(Create(server_box), Create(cross), Write(s_label))

        badge = Rectangle(height=0.8, width=8.5, color=GOLD).to_edge(DOWN)
        b_txt = Text("100% Air-Gapped Privacy | 0ms Network Latency | 48 tokens/sec", font_size=18, color=GOLD).move_to(badge)
        self.play(Create(badge), Write(b_txt))
        self.wait(2)
