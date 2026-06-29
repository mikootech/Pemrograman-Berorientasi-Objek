import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Palet warna hangat yang senada dengan tema aplikasi
WARNA_PEMASUKAN = "#6B9E64"     # Hijau sage lembut
WARNA_PENGELUARAN = "#C27A6A"   # Merah redup/muted

WARNA_KATEGORI = [
    "#E8915A",   # Orange soft
    "#D4A24C",   # Gold
    "#C27A6A",   # Merah redup
    "#A3C9A8",   # Sage green
    "#E8A99A",   # Salmon soft
    "#F0D590",   # Gold muda
]

# Layout dasar yang dipakai semua chart
LAYOUT_DASAR = dict(
    font=dict(family="Inter, sans-serif", color="#3D2B1F"),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(t=30, b=20, l=20, r=20),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.25,
        xanchor="center",
        x=0.5,
        font=dict(size=12, color="#7A6455"),
        bgcolor="rgba(0,0,0,0)",
    ),
)


def buat_grafik_donat_kategori(df_pengeluaran):
    """Membuat grafik donat (pie chart berlubang) menggunakan Plotly."""
    if df_pengeluaran.empty:
        return None

    data_grup = df_pengeluaran.groupby('kategori')['jumlah'].sum().reset_index()

    fig = go.Figure(
        go.Pie(
            labels=data_grup['kategori'],
            values=data_grup['jumlah'],
            hole=0.55,
            marker=dict(
                colors=WARNA_KATEGORI[:len(data_grup)],
                line=dict(color="#FFFAF5", width=3),
            ),
            textinfo="percent+label",
            textfont=dict(size=13, color="#3D2B1F"),
            hovertemplate="<b>%{label}</b><br>"
                          "Rp %{value:,.0f}<br>"
                          "%{percent}<extra></extra>",
            pull=[0.03] * len(data_grup),
        )
    )

    # Tambah teks di tengah donat
    fig.update_layout(
        **LAYOUT_DASAR,
        showlegend=True,
        annotations=[
            dict(
                text="<b>Total</b>",
                x=0.5, y=0.5,
                font=dict(size=14, color="#7A6455"),
                showarrow=False,
            )
        ],
        height=350,
    )
    return fig


def buat_grafik_bar_bulanan(df):
    """Membuat grafik batang perbandingan Pemasukan vs Pengeluaran per tanggal."""
    if df.empty:
        return None

    data_grup = df.groupby(['tanggal', 'jenis'])['jumlah'].sum().reset_index()

    fig = go.Figure()

    # Bar Pemasukan
    df_masuk = data_grup[data_grup['jenis'] == 'pemasukan']
    fig.add_trace(
        go.Bar(
            x=df_masuk['tanggal'],
            y=df_masuk['jumlah'],
            name="Pemasukan",
            marker=dict(
                color=WARNA_PEMASUKAN,
                cornerradius=6,
                line=dict(width=0),
            ),
            hovertemplate="<b>%{x}</b><br>"
                          "Pemasukan: Rp %{y:,.0f}<extra></extra>",
        )
    )

    # Bar Pengeluaran
    df_keluar = data_grup[data_grup['jenis'] == 'pengeluaran']
    fig.add_trace(
        go.Bar(
            x=df_keluar['tanggal'],
            y=df_keluar['jumlah'],
            name="Pengeluaran",
            marker=dict(
                color=WARNA_PENGELUARAN,
                cornerradius=6,
                line=dict(width=0),
            ),
            hovertemplate="<b>%{x}</b><br>"
                          "Pengeluaran: Rp %{y:,.0f}<extra></extra>",
        )
    )

    fig.update_layout(
        **LAYOUT_DASAR,
        barmode="group",
        bargap=0.25,
        bargroupgap=0.08,
        xaxis=dict(
            title="",
            showgrid=False,
            tickfont=dict(size=11, color="#7A6455"),
        ),
        yaxis=dict(
            title="",
            showgrid=True,
            gridcolor="rgba(212,162,76,0.1)",
            gridwidth=1,
            tickfont=dict(size=11, color="#A89585"),
            tickformat=",.0f",
        ),
        height=350,
    )
    return fig
